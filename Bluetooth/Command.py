from Bluetooth.Commands import Commands

class Command():
    command_id = Commands.STOP
    command_value = None

    def __init__(self, command_id, value=None):
        self.command_id = command_id
        self.command_value = value

    def __str__(self):
        if self.command_value:
            return f"{self.command_id} with value {self.command_value}"
        else:
            return self.command_id
