import serial


class UartSender:
    connection = None

    def __init__(self,device,baundRate):
        self.connection = serial.Serial(device)
        self.connection.baudrate = baundRate
        self.connection.timeout = 1        #non-block read
        self.connection.writeTimeout = 1   #timeout for write
        print "UartSender constructed (", device, " at ",baundRate,")"

# OTHER OPTIONS
#        self.connection.bytesize = serial.EIGHTBITS #number of bits per bytes
#        self.connection.parity = serial.PARITY_NONE #set parity check: no parity
#        self.connection.stopbits = serial.STOPBITS_ONE #number of stop bits
#        self.connection.xonxoff = False     #disable software flow control
#        self.connection.rtscts = False     #disable hardware (RTS/CTS) flow control
#        self.connection.dsrdtr = False       #disable hardware (DSR/DTR) flow control

    def send(self, message):
        self.connection.write(message)
        self.printMSG(message)
        #self.readANS()

    def printMSG(self,message):
        i=0
        sep=[4,8,12,16,20,23]
        print " - ",
        for b in message:
          if i in sep: print "|",
          print b.encode('hex'),
          i=i+1

    def readANS(self):
        try:
          ans = self.connection.readline()   # read a '\n' terminated line
          if not ans:
            raise  Error('no ans')
          else:
            print 'UART: "',str(ans).rstrip(),'"'
        except:
          print 'UART: no response'


    def closeConnection(self):
        self.connection.close()
