from tests.test_rover import do_tests as rover_do_tests
from tests.test_message_service import do_tests as ms_do_tests
from tests.test_messages import print_test_messages
from tests.test_command_service import do_tests as cs_do_tests
from tests.test_rover_service_controllers import do_tests as rs_controllers_do_tests
from tests.test_control_pad_controller import do_tests as control_pad_controller_do_tests
def do_tests():
    ### Rover Tests - use this to test the Rover module and system function.
    ### Inspect the tests/rover_tests folder for help on using the rover interfaces.
    #rover_do_tests()

    ### Test Message Service - smartphone connection is required.
    ### Press LED OFF to end test. Bluetooth messages are displayed.
    #ms_do_tests()

    ### Show Test Messages - these are a list of test messages used in command service
    ### testing so that a connection to your smartphone is not required.
    #print_test_messages()

    ### Test Command Service - uses bluetooth test messages above")
    ### to verify messsage to command objects conversion.")
    #cs_do_tests()

    ### Test Rover Service Controller - uses Mode messages to swap controllers
    rs_controllers_do_tests()

    ###################################################
    ### NOTE - THE FOLLOWING TESTS WILL FAIL UNTIL  ### 
    ### YOU IMPLEMENT THE REQUIRED CONTROLLERS      ###
    ###################################################
    #control_pad_controller_do_tests()


if __name__ == "__main__":
    do_tests()