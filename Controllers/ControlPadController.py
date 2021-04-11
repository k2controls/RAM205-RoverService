''' Control Pad controller
'''
from Controllers.Controller import Controller
from Bluetooth.Commands import Command_ID
from Rover.RoverDrive import DriveMotion
from Rover.Buzzer import BuzzerStatus
from Rover.LED import LEDStatus
from Rover.RGBLed import LED_COLOR

class ControlPadController(Controller):
    def __init__(self, rover):
        self.rover = rover

    def update(self, command):
        self.last_command = command
        print(f">>>CommandID={command.command_id}, Value={command.value}")

        if command.command_id == Command_ID.BEEP:
            self.rover.buzzer.toggle()
