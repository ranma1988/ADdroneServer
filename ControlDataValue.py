from struct import *
from CommDataValue import CommDataValue
from ControlData import ControlData

class ControlDataValue(CommDataValue):

    # control communication data struct
    messageFormat = '<4s3ffHB13sH'
    # example: ('$$$$', 0.0, 0.0, 0.0, 0.0, 1000, 10, 1, 65535)
    # '<'         encoding = network = big endian
    # 0     '4s'        # preamble $$$$
    # 1,2,3 '3f'        # roll, pitch, yaw
    # 4     'f'         # throtthe
    # 5     'H'         # controller command
    # 6     'B'         # solver mode
    # 7     '13s'       # dummy 
    # 8     'H'         # crc

    roll = 0.0
    pitch = 0.0
    yaw = 0.0

    throttle = 0.0

    controllerCommand = 0
    solverMode = 0
    
    def __init__(self, controlData = None):
        self.preamble = "$$$$"
        if controlData is not None:
            values = unpack(self.messageFormat, controlData.getData()) 
            self.preamble = values[0]
            self.roll = values[1]
            self.pitch = values[2]
            self.yaw = values[3]
            self.throttle = values[4]
            self.controllerCommand = values[5]
            self.solverMode = values[6]
            self.CRC = values[8]

    def getCommData(self):
        data = pack(self.messageFormat,
            self.preamble, 
            self.roll, self.pitch, self.yaw,
            self.throttle,
            self.controllerCommand,
            self.solverMode,
            "\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff", # padding
            self.CRC)
        return ControlData(data)

    def toString(self):
        return "(rpy: ({0:.2f},{1:.2f},{2:.2f}), th: {3:.2f}, cmd: {4:d} CRC: 0x{5:04X})".format(
            self.roll, self.pitch, self.yaw,
            self.throttle,
            self.controllerCommand,
            self.CRC)

    @staticmethod
    def StopCommand():
        data = pack(ControlDataValue.messageFormat,
                    "$$$$",
                    0.0, 0.0, 0.0, 0.0, #roll pith yaw throttle
                    2000,               # cmd
                    1,                  # solver mode
                    "\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff",    #padding
                    0x727a)             #crc
        return ControlData(data)

    @staticmethod
    def SomeValidControlCommand():
        data = pack(ControlDataValue.messageFormat,
                    "$$$$",
                    0.0, 0.0, 0.0, 0.4, #roll pith yaw throttle
                    1000,               # cmd
                    1,                  # solver mode
                    "\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff",    #padding
                    0x4588)             #crc
        return ControlData(data)
