from DebugData import *

class FakeUartSender:
    connection = None
    to_recv = ""

    def __init__(self):
        print('FakeUartSender constructed')

    def send(self, message):
        pass
        # self.to_recv += message

    def recv(self):
        data = DebugData.SomeValidDebugData().data
        # data = self.to_recv
        # self.to_recv = ""
        return data

    # TODO check if this method is needed
    def closeConnection(self):
        print('Connection closed')
