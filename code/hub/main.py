import sys
import time

from communications.scanner import Scanner
from sensors.sensor import Sensor

SEC_BETWEEN_SCANS = 1


def add_sensors(i2c_addresses, sensors):
    for address in i2c_addresses:
        new_sensor = Sensor(address)
        new_sensor.initialize()
        return sensors.add(new_sensor)


def main():
    print("Comparative air pollution sensor v. 0.1 starting...")
    print("Python version:")
    print(sys.version)
    if len(sys.argv) < 2:
        print("Usage : main.py <bus>")
        sys.exit()
    bus = int(sys.argv[1])
    scanner = Scanner(bus)
    start_addr, end_addr = 0, 127
    print("Going to scan I2C network for live sensors.")
    print(f"Start address: {hex(start_addr)}")
    print(f"End address:  {hex(end_addr)}\n")
    addresses = set()
    sensors = set()
    while True:
        new_addresses = scanner.scan(start_addr, end_addr)
        added, vanished = new_addresses - addresses, addresses - new_addresses
        if len(added) > 0:
            print(f"New hosts: {added}")
            sensors = add_sensors(added, sensors)
        if len(vanished) > 0:
            print(f"Vanished hosts: {vanished}")
            sensors = {x for x in sensors if x.addr in vanished}
        addresses = new_addresses
        time.sleep(SEC_BETWEEN_SCANS)


if __name__ == "__main__":
    main()
