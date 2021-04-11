''' RGBLed Class
Implements Red, Green, Blue LED.
Uses LED class
'''
from Rover.LED import LED, LEDStatus
from enum import Enum

class LED_COLOR(Enum):
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

    def __init__(self, red_led: LED, green_led: LED, blue_led: LED):
        self.red_led = red_led
        self.green_led = green_led
        self.blue_led = blue_led
        self.status = LED_COLOR.OFF

    def __str__(self):
        s = f"Red {self.red_led.__str__()}, " \
            f"Green {self.green_led.__str__()}, " \
            f"Blue {self.blue_led.__str__()}."
        return s

    def set_color(self, color: LED_COLOR):
        self.red_led.update(color.value[0])
        self.green_led.update(color.value[1])
        self.blue_led.update(color.value[2])

    def get_color_value(self):
        c = (int(self.red_led.is_on()), int(self.green_led.is_on()), int(self.blue_led.is_on()))
        return c
    

