from Bluetooth.Commands import Command_Type, Command_ID


class Command():

    def __init__(self, command_type: Command_Type, command_id: Command_ID, value=0, message=""):
        self.command_type = command_type
        self.command_id = command_id
        self.value = value
        self.message = message

    def __str__(self):
        if self.command_type == Command_Type.ANALOG:
            return f"{self.command_id.name} (value = {self.value})."
        else:
            return self.command_id.name
