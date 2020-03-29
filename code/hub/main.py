import argparse
import sys
import time

from communications.scanner import Scanner
from sensors.sensor import Sensor

SEC_BETWEEN_SCANS = 1


def main():
    print_welcome_msg()
    args = parse_args()
    bus = args.bus
    print(f"I2C bus: {bus}")
    scanner = Scanner(bus)
    print(
        f"Going to scan I2C network for live sensors "
        f"every {SEC_BETWEEN_SCANS} second(s)."
    )
    print(f"Start address: {scanner.start_addr} ({hex(scanner.start_addr)})")
    print(f"End address: {scanner.end_addr} ({hex(scanner.end_addr)})\n")
    addresses = set()
    sensors = set()
    while True:
        new_addresses = scanner.scan()
        added, vanished = new_addresses - addresses, addresses - new_addresses
        if len(added) > 0:
            print(f"New nodes: {added}")
            for address in added:
                print(f"Registering with sensor {address}@{bus}...")
                s = Sensor(bus, address)
                print(
                    f"Sensor {address}@{bus}: UUID {s.uuid}, model {s.model}, "
                    f"pollutants {s.pollutants}, "
                    f"sample period {s.sample_period_seconds} seconds."
                )
                sensors.add(s)
        if len(vanished) > 0:
            print(f"Vanished nodes: {vanished}")
            sensors = {x for x in sensors if x.address not in vanished}
        addresses = new_addresses
        time.sleep(SEC_BETWEEN_SCANS)


def parse_args():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument(
        "-b",
        "--bus",
        type=int,
        help="I2C bus number. "
        "On Raspberry Pi it can be determined with `ls /dev/*i2c*`",
    )
    return parser.parse_args()


def print_welcome_msg():
    print("\nComparative air pollution sensor v. 0.1 starting...")
    print("Python version:")
    print(sys.version)
    print("Arguments:")
    print(sys.argv)
    print()


if __name__ == "__main__":
    main()
