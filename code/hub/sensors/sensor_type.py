from enum import Enum


class SensorType(str, Enum):
    PPD42 = "Shinyei PPD42"
    PMS3003 = "PMS3003"
    PMS5003 = "PMS5003"
    PMS7003 = "PMS7003"
    HPMA115S0 = "HPMA115S0"
