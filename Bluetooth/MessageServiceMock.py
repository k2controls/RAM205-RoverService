''' Message Service Mock
Mocks message service using list of test messages
'''
from Bluetooth.bluetooth_test_messages import bluetooth_test_messages

class MessageService():

    def __init__(self):
        self.test_messages = bluetooth_test_messages
            
    def get_message(self):
        #wait for start
        input_str = "0,0,0,0,0,0,0,0,0"            #STOP
        if len(self.test_messages):
            input_str = self.test_messages.pop(0)
        return input_str
