import argparse
import sys
import threading
import time

from gui.gui import gui_loop
from sensors.iic_scanner import IicScanner
from sensors.sensor import Sensor

sensors = set()


def print_welcome_msg():
    print("\nComparative air quality sensor v. 0.1 starting...")
    print("Python version:")
    print(sys.version)
    print("Arguments:")
    print(sys.argv)
    print()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-b",
        "--bus",
        type=int,
        help="I2C bus number. "
        "On Raspberry Pi it can be determined with `ls /dev/*i2c*`",
    )
    parser.add_argument(
        "-sp",
        "--scan-period",
        type=int,
        help="I2C bus will be scanned for changes this often. Unit: seconds.",
        default=1,
    )
    parser.add_argument(
        "-rp",
        "--redraw-period",
        type=int,
        help="Plot will be refreshed this often. Unit: seconds.",
        default=1,
    )
    return parser.parse_args()


def i2c_scan_loop(bus, period):
    print(f"I2C bus: {bus}")
    print(f"Going to scan I2C network for live sensors every {period} second(s).")

    scanner = IicScanner(bus)
    print(f"Start address: {scanner.start_addr} ({hex(scanner.start_addr)})")
    print(f"End address: {scanner.end_addr} ({hex(scanner.end_addr)})\n")

    addresses = set()
    global sensors
    while True:
        new_addresses = scanner.scan()
        added, vanished = new_addresses - addresses, addresses - new_addresses
        if added:
            print(f"New nodes: {added}")
            for address in added:
                print(f"Registering with (presumably) sensor {address}@{bus}...")
                s = Sensor(bus, address)
                if s.ok:
                    print(
                        f"Sensor {address}@{bus}: UUID {s.uuid}, model {s.model}, "
                        f"pollutants: {s.pollutants}, "
                        f"sample period {s.sample_period_seconds} seconds."
                    )
                    sensors.add(s)
                else:
                    print(
                        f"Device {address}@{bus} is not a sensor! "
                        f"Could not get the required data out of it."
                    )
                addresses.add(address)
        if vanished:
            print(f"Vanished nodes: {vanished}")
            sensors = {x for x in sensors if x.address not in vanished}
            addresses -= vanished
        time.sleep(period)


if __name__ == "__main__":
    print_welcome_msg()
    args = parse_args()
    i2c_bus, i2c_scan_period, redraw_period = (
        args.bus,
        args.scan_period,
        args.redraw_period,
    )
    i2c_scan_thread = threading.Thread(target=i2c_scan_loop(i2c_bus, i2c_scan_period))
    i2c_scan_thread.start()
    gui_loop(redraw_period)
    i2c_scan_thread.join()
