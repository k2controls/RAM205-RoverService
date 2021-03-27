''' Servo Class
Implements basic servo action
'''
import RPi.GPIO as GPIO 

class Servo():
    _pin = None
    ccw_position_value = 0
    cw_position_value = 180

    def __init__(self, pin):
        self._pin = pin
        #TODO config servo pin

    def __del__(self):
        GPIO.cleanup()

    def rotate(self, position):
        #TODO implement rotate
        pass
    
