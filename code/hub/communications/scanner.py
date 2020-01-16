from smbus2 import SMBus


class Scanner:
    """
    Scan I2C network on specified bus for live hosts,
    respecting reserved addresses.
    """

    def __init__(self, bus_num):
        self.bus_num = bus_num
        print("I2C bus  :" + str(bus_num))

    def scan(self, start_addr=0x00, end_addr=0x7F):
        """ Scan I2C bus, return the list of live host addresses"""
        try:
            bus = SMBus(self.bus_num)
        except PermissionError:
            print("Permission error!")
            return []

        live_hosts = set()
        reserved_addresses = {0, 1, 2, 3, 4, 5, 6, 7,
                              120, 121, 122, 123, 124, 125, 126, 127}
        for i in {item for item in range(start_addr, end_addr + 1)
                  if item not in reserved_addresses}:
            val = 1
            try:
                bus.read_byte(i)
            except OSError as e:
                val = e.args[0]
            finally:
                if val == 1:
                    live_hosts.add(i)
        return live_hosts
