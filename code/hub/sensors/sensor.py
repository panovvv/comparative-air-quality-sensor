from enum import Enum

from smbus2 import SMBus, i2c_msg
from smbus2.smbus2 import I2C_SMBUS_BLOCK_MAX


class Pollutant(str, Enum):
    PM01 = "PM0.1"
    PM1 = "PM1"
    PM25 = "PM2.5"
    PM10 = "PM10"
    CO = "CO"
    SO2 = "SO2"
    O3 = "O3"
    NO2 = "NO2"

    @staticmethod
    def from_str(val):
        try:
            return Pollutant(val)
        except ValueError:
            if val == "PM1.0":
                return Pollutant.PM1
            elif val == "SO":
                return Pollutant.SO2
            elif val == "NO":
                return Pollutant.NO2
            else:
                raise


class Sensor:
    def __init__(self, bus, address):
        self.bus = bus
        self.address = address
        try:
            self.uuid = self.__get_from_sensor("uuid")
            self.model = self.__get_from_sensor("model")
            self.pollutants = []
            pollutants_str = self.__get_from_sensor("pollutants")
            for pollutant in pollutants_str.split(","):
                try:
                    self.pollutants.append(Pollutant.from_str(pollutant))
                except ValueError:
                    print(
                        f"Sensor {self.address}@{self.bus} sent an "
                        f"unrecognized pollutant: {pollutant}"
                    )
            self.sample_period_seconds = self.__get_from_sensor("sample_period_seconds")
            self.ok = True
        except IOError:
            self.ok = False

    def get_measurements(self):
        # TODO EACH MEASUREMENT HAS UUID IN IT
        return {(p, self.__get_from_sensor(p)) for p in self.pollutants}

    def __get_from_sensor(self, what: str):
        write = i2c_msg.write(self.address, list(f"get_{what}".encode("ascii")))
        read = i2c_msg.read(self.address, I2C_SMBUS_BLOCK_MAX)
        with SMBus(self.bus) as bus:
            bus.i2c_rdwr(write)
            bus.i2c_rdwr(read)
            return str(read).strip().strip("\0")
