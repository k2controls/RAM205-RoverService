import time
from Bluetooth.MessageService import MessageService
from Bluetooth.CommandService import CommandService
from Rover.rover_factory import make_rover
from RoverService import RoverService
from Bluetooth.Commands import Command_ID

def main():

    message_service = MessageService()
    command_queue = list()
    cs = CommandService(message_service ,command_queue)
    rover = make_rover()
    rover_service = RoverService(cs,rover)
    #press LED OFF twice to exit
    while True:
        if rover_service.last_command == rover_service.command == Command_ID.LED_OFF:
            break
        time.sleep(.5)

if __name__ == "__main__":
    main()