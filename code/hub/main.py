import sys
import time

from communications.scanner import Scanner

SEC_BETWEEN_SCANS = 1


def main():
    print("Comparative air pollution sensor v 0.1 starting...")
    args = sys.argv
    if len(args) < 2:
        print("Specify desired I2C bus!")
        print("Usage : main.py <bus>")
        sys.exit()
    bus = int(args[1])
    scanner = Scanner(bus)
    start_addr = 0
    end_addr = 127
    print("Going to scan I2C network for live sensors.")
    print("Start address : " + hex(start_addr))
    print("End address   : " + hex(end_addr) + "\n")
    addresses = set()
    while True:
        new_addresses = scanner.scan(start_addr, end_addr)
        added = new_addresses - addresses
        vanished = addresses - new_addresses
        if len(added) > 0:
            print("New hosts:")
            print(added)
        if len(vanished) > 0:
            print("Vanished hosts:")
            print(vanished)
        addresses = new_addresses
        time.sleep(SEC_BETWEEN_SCANS)


if __name__ == "__main__":
    main()
