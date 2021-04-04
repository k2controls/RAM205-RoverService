''' piRover Bluetooth module
Provides interface to Yahboom smartphone
app enabling remote control of the piRover.

Keith E. Kelly
V2 - 3/12/21
    - added mode string and gimbal motion
'''
import time
from serial import Serial
from threading import Thread
from enum import Enum
from messages import mode_messages, analog_messages, button_messages
from Commands import Commands
from Command import Command

class Bluetooth(Thread):

    def __init__(self, command_queue: list):
        self.serial = Serial("/dev/ttyAMA0", 9600)
        Thread.__init__(self)
        self.command_queue = command_queue
        self.daemon = True
        self.start()
    
    def run(self):
        while True:
            message_string = self._get_message_string()
            commands = self._make_commands(message_string)
            self.command_queue.append(commands)
            
    def _get_message_string(self):
        #wait for start
        input_str = ""
        while self.serial.read(1).decode() != "$":
            pass
        #wait for end
        while True:
            char = self.serial.read(1).decode()
            if char == "#":
                break
            input_str += char
        return input_str

    def _make_commands(self, message):
        commands = []   #list of commands due to rgb message creating 3 analog cmds
        if message.count("4WD") and message.count("MODE"):
            # this is a mode message
            command_id = mode_messages[message]
            command = Command(command_id)
            commands.append(command)
        elif message.count("4WD"):
            # this is an analog message
            seg = message.split(",")
            if len(seg) == 4:   #rgb analog color message
                # red first
                red = seg[1]
                value = int(red[3:])
                command = Command(Commands.LED_RED_ANALOG, value)
                commands.append(command)
                #green
                green = seg[2]
                value = int(green[3:])
                command = Command(Commands.LED_GREEN_ANALOG, value)
                commands.append(command)
                #blue
                blue = seg[3]
                value = int(blue[3:])
                command = Command(Commands.LED_BLUE_ANALOG, value)
                commands.append(command)               
            elif len(seg) == 2:     #analog servo message
                servo = seg[1]
                value = int(servo[3:])
                command = Command(Commands.SERVO_ANALOG, value)
            else:
                raise ValueError("Invalid message format.")
        else: # Control pad button message
            command_id = button_messages[message]
            command = Command(command_id)
            commands.append(command)

        return commands
        