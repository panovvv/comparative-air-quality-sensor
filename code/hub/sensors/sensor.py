from sensors.communication_error import CommunicationError
from sensors.sensor_type import SensorType


class Sensor:
    """TODO"""

    def __init__(self, address):
        self.address = address
        self.sensor_type = None

    def initialize(self):
        """

        :return:
        """
        print(f"Registering with {self.sensor_type} sensor @ {self.address}")
        self.sensor_type = SensorType.ppd42
        if self.sensor_type is None:
            raise CommunicationError("Sensor type unknown!")
