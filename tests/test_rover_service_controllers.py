''' Runs bluetooth tests
'''
import time
from Bluetooth.MessageServiceMock import MessageService
from Bluetooth.CommandService import CommandService
from Rover.rover_factory import make_rover
from RoverService import RoverService
from Controllers.ControlPadController import ControlPadController
from Controllers.CameraController import CameraController
from Controllers.ColorfulController import ColorfulController
from Controllers.ObstacleController import ObstacleController
from Controllers.TrackerController import TrackerController
from Rover.RoverDrive import DriveMotion

message_service = None
rover_service = None

def make_rover_service():
    global message_service, rover_service
    
    message_service = MessageService()
    command_queue = list()
    cs = CommandService(message_service ,command_queue)
    rover = make_rover()
    rover_service = RoverService(cs,rover)
    
def test_default_controller():
    print("Checking default controller...")
    if type(rover_service.controller) == ControlPadController:
        print("Default controller test passed.")
        return True
    else:
        print(f"Default controller test failed. type={type(rover_service.controller)}")
        return False

def test_switch_controller(mode_message, controller_type):
    print(f"\nSwitching to controller {controller_type}...")
    message_service.set_message(mode_message)
    time.sleep(10)
    if type(rover_service.controller) == controller_type:
        print(f"\nSwitch controller test passed. type={type(rover_service.controller)}")
        return True
    else:
        print(f"\nSwitch controller test failed. type={type(rover_service.controller)}")
        return False
    
def do_tests():
    non_mode_message = "0,0,0,0,0,0,0,0,0"
    make_rover_service()
    if not test_default_controller():
        print("Failed!")
    elif not test_switch_controller("4WD,MODE41", ColorfulController):
        print("Failed!")
    elif not test_switch_controller("4WD,MODE31", ObstacleController):
        print("Failed!")
    elif not test_switch_controller("4WD,MODE21", TrackerController):
        print("Failed!")
    elif not test_switch_controller(non_mode_message, ControlPadController):
        # any none-mode message when controller is not control pad 
        # switches controller back to default control pad controller
        print("Failed!")
    else:
        print("Rover service controller tests passed.")
        print()
    


