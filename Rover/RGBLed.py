''' RGBLed Class
Implements Red, Green, Blue LED.
Uses LED class
'''
from Rover.LED import LED

class LED_COLOR():
    ''' Tuples defining RGB states for basic colors (R, G, B)
    '''
    OFF =       (0, 0, 0)
    RED =       (1, 0, 0)
    GREEN =     (0, 1, 0)
    BLUE =      (0, 0, 1)
    AMBER =     (1, 1, 0)
    CYAN =      (0, 1, 1)
    MAGENTA =   (1, 0, 1)
    WHITE =     (1, 1, 1)

class RGBLed():

    def __init__(self, redLED: LED, greenLED: LED, blueLED: LED):
        self.redLED = redLED
        self.greenLED = greenLED
        self.blueLED = blueLED

    def set_color(self, color: LED_COLOR):
        self.redLED.update(color[0])
        self.greenLED.update(color[1])
        self.blueLED.update(color[2])

