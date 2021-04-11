from tests.test_messages import bluetooth_test_messages
from Bluetooth.MessageServiceMock import MessageService
from Bluetooth.CommandService import CommandService
import time

def do_tests():
    print("Test Command Service using bluetooth test messages")
    print("Sample messages are converted to command objects in a background thread.")
    ms = MessageService(bluetooth_test_messages)
    commands = list()
    cs = CommandService(ms, commands)
    time.sleep(1)
    for command in commands:
        print(f"{command.command_type}\t{command.command_id}\t\t{command.value}\t{command.message}")
        time.sleep(.5)

