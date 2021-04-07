''' Contains tests for Rover Bluetooth functions
No testing framework used. First test prints inputs 
from Bluetooth serial. Other tests use bluetooth_test_messages
to test command services
'''
import time
from Bluetooth.MessageService import MessageService
#from Bluetooth.MessageServiceMock import MessageService
from Bluetooth.CommandService import CommandService

TEST_COUNT = 30

def bluetooth_messages_test():
    # prints first TEST_COUNT messages from bluetooth serial connection
    # phone must be connected and used to create input
    ms = MessageService()
    for i in range(TEST_COUNT):
        message = ms.get_message()
        print(message)

def command_service_test():
    # prints commands based on first TEST_COUNT messages from bluetooth 
    # serial connection.
    # phone must be connected and used to create input
    ms = MessageService()
    commands_list = list()
    cs = CommandService(ms, commands_list)
    for i in range(TEST_COUNT):
        while len(commands_list) == 0:
            time.sleep(1)
        command = commands_list.pop(0) 
        print(f"Command: {command.command_id}\t\t Value: {command.command_value}")    

