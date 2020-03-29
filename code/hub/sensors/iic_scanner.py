from smbus2 import SMBus

RESERVED_ADDR = {
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    120,
    121,
    122,
    123,
    124,
    125,
    126,
    127,
}


class IicScanner:
    """
    Scan I2C network on specified bus for live hosts,
    respecting reserved addresses.
    """

    def __init__(self, bus_num, start_addr=0x00, end_addr=0x7F):
        self.bus_num = bus_num
        self.start_addr = start_addr
        self.end_addr = end_addr

    def scan(self):
        """Scan I2C bus, return the list of live host addresses"""
        try:
            bus = SMBus(self.bus_num)
        except PermissionError as pe:
            print(f"Permission error:\n{pe}")
            return []

        live_hosts = set()
        for i in {
            item
            for item in range(self.start_addr, self.end_addr + 1)
            if item not in RESERVED_ADDR
        }:
            val = 1
            try:
                bus.read_byte(i)
            except OSError as e:
                val = e.args[0]
            finally:
                if val == 1:
                    live_hosts.add(i)
        return live_hosts
