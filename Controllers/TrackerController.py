''' Tracker Controller
'''
from threading import Thread
from Rover.RGBLed import RGBLed, LED_COLOR
import time

class TrackerController(Thread):
    def __init__(self, rover):
        self.rover = rover
        self.go = True
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        while self.go:
            self.rover.rgb_led.set_color(LED_COLOR.GREEN)
            print("z", end="")
            time.sleep(1)
            self.rover.rgb_led.set_color(LED_COLOR.OFF)
            print("-", end="")
            time.sleep(1)
        
    def teardown(self):
        self.go = False