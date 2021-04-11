''' Base class for Rover Modes
'''
from Rover.Rover import Rover
from Bluetooth.Command import Command

class Controller():
    def __init__(self, rover):
        self.rover = rover
        self.last_command = None

    def update(self, command: Command):
        self.last_command = command

    def teardown(self):
        self.rover = None
        self.last_command = None
