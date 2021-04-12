''' Rover Service

'''
import time
from threading import Thread
from Controllers.ControlPadController import ControlPadController
from Controllers.ColorfulController import ColorfulController
from Controllers.TrackerController import TrackerController
from Controllers.ObstacleController import ObstacleController
from Bluetooth.Commands import Command_Type, Command_ID

class RoverService(Thread):

    def __init__(self, command_service, rover):
        self.command_service = command_service
        self.rover = rover
        self.last_command = None
        self.command = None
        self.controller = ControlPadController(self.rover)
        Thread.__init__(self)
        self.daemon = True
        self.start()
        
    def run(self):
        while True:
            if self.command_service.command_queue:
                self.last_command = self.command
                self.command = self.command_service.command_queue.pop(0)
                self.do_command(self.command)
               
    def do_command(self, command):
        if command.command_type == Command_Type.MODE:
            self.switch_controller(command)
        elif type(self.controller) == ControlPadController:
            self.controller.update(command)
        else:
            self.switch_controller(command)
        
    def switch_controller(self, command):
        self.controller.teardown()
        if command.command_id == Command_ID.COLORFUL_START:
            self.controller = ColorfulController(self.rover)
        elif command.command_id == Command_ID.TRACTING_START:
            self.controller = TrackerController(self.rover)
        elif command.command_id == Command_ID.OBSTACLE_START:
            self.controller = ObstacleController(self.rover)
        else:
            self.controller = ControlPadController(self.rover)
        