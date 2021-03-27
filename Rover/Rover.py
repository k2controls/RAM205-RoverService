''' Rover Class
Container used to encapsulate all rover objects
'''

class Rover():

    def __init__(self):
        self.buzzer = None
        self.camera = None   #???
        self.gimbal = None
        self.line_follower = None
        self.rgb_led = None
        self.rover_drive = None
        self.servo = None
        self.sonar_ping = None
        self.warner = None

    def__del__(self):
        self.buzzer = None
        self.camera = None
        self.gimbal = None
        self.line_follower = None
        self.rgb_led = None
        self.rover_drive = None
        self.servo = None
        self.sonar_ping = None
        self.warner = None
