import serial


class UartController:
    connection = None

    def __init__(self,device,baundRate):
        self.connection = serial.Serial(device)
        self.connection.baudrate = baundRate
        self.connection.timeout = 1        #non-block read
        self.connection.writeTimeout = 1   #timeout for write
        self.connection.bytesize = serial.EIGHTBITS #number of bits per bytes
        self.connection.parity = serial.PARITY_NONE #set parity check: no parity
        self.connection.stopbits = serial.STOPBITS_ONE #number of stop bits
        print "UartSender: constructed (", device, " at ",baundRate,")"

# OTHER OPTIONS
#        self.connection.xonxoff = False     #disable software flow control
#        self.connection.rtscts = False     #disable hardware (RTS/CTS) flow control
#        self.connection.dsrdtr = False       #disable hardware (DSR/DTR) flow control

    def send(self, message):
        self.connection.write(message)

    def recv(self):
        data = ''
        nbBytesWaitingInInputBuffer = self.connection.inWaiting()
        print "to read: ", nbBytesWaitingInInputBuffer
        if nbBytesWaitingInInputBuffer > 0:
            try:
                data = self.connection.read(nbBytesWaitingInInputBuffer)
            except:
                print('UART: read timeout or error')
        return data

    def close(self):
        self.connection.close()