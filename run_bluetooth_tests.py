''' Runs bluetooth tests
'''
from Tests.bluetooth_tests import *

def do_tests():
    bluetooth_messages_test()
    #bluetooth_message_mock_test()
    command_service_test()
    #command_service_test_with_mock()


if __name__ == "__main__":
    do_tests()