''' Rover Service

'''
import time
from Controllers.ControlPadController import ControlPadController
from Controllers.ColorfulController import ColorfulController
from Controllers.TrackerController import TrackerController
from Controllers.ObstacleController import ObstacleController
from Bluetooth.Commands import Commands

class RoverService():

    def __init__(self, command_service, rover):
        self.command_service = command_service
        self.rover = rover
        self.controller = ControlPadController
        self.controller.start(self.rover)

    def run(self):
        while not len(self.command_service.command_queue):
            time.sleep(.1)
        command = self.command_service.command_queue.pop(0)
        self.do_command(command)

    def do_command(self, command):
        if command.is_mode_message():
            self.switch_controller(command)
        elif type(self.controller) == ControlPadController:
            self.controller.update(command)
        else:
            self.switch_controller(command)
        

    def switch_controller(self, command):
        self.controller.teardown()
        if command.command_id == Commands.COLORFUL_START:
            self.controller = ColorfulController()
        elif command.command_id == Commands.TRACTING_START:
            self.controller = TrackerController()
        elif command.command_id == Commands.OBSTACLE_START:
            self.controller = ObstacleController()
        else:
            self.controller = ControlPadController()
        self.controller.start(self.rover)