import sys

from smbus2 import SMBus


def scan(bus_num, start=0x03, end=0x78):
    try:
        bus = SMBus(bus_num)
    except PermissionError:
        print("Permission error!")
        sys.exit()

    print("I2C bus       : " + str(bus_num))
    print("Start address : " + hex(start))
    print("End address   : " + hex(end) + "\n")

    for i in range(start, end):
        val = 1
        try:
            bus.read_byte(i)
        except OSError as e:
            val = e.args[0]
        finally:
            if val == 1:
                res = "Available"
            elif val == 16:
                res = "Busy"
            elif val == 110:
                res = "Timeout"
            else:
                res = "Error code: " + str(val)
            if val == 1 or val == 16 or val == 110:
                print(hex(i) + " -> " + res)
