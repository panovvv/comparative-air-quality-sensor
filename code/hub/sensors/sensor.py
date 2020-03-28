from sensors.communication_error import CommunicationError
from sensors.sensor_type import SensorType


class Sensor:
    def __init__(self, address):
        self.address = address
        self.sensor_type = None
        self.__initialize()

    def __initialize(self):
        self.sensor_type = SensorType.PPD42
        print(f"Registering with {self.sensor_type} sensor @ {self.address}")
        if self.sensor_type is None:
            raise CommunicationError("Sensor type unknown!")
