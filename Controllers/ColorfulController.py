''' Colorful Controller class
'''
import time
from Rover.RGBLed import RGBLed, LED_COLOR
from threading import Thread

class ColorfulController(Thread):
    def __init__(self, rover):
        self.rover = rover
        self.go = True
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        ''' TODO RAM205 FINAL
            Complete this run method to implement the colorful search
            as implemented in the orignal Yaboom solutions.
            Just come close, updating with all RGB colors while moving servo
            Do your own work. Do not share your solution.
        '''    
        while self.go:
            # this code is for demo only. Delete as required
            self.rover.rgb_led.set_color(LED_COLOR.WHITE)
            print("x", end="")
            time.sleep(1)
            self.rover.rgb_led.set_color(LED_COLOR.OFF)
            print("-", end="")
            time.sleep(1)

    def teardown(self):
        self.go = False