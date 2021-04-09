''' Line Follower class
Senses line follower inputs and define
next drive motion
'''
#from Rover import RoverDrive
from Rover.RoverDrive import Motion
import RPi.GPIO as GPIO
from Rover.RoverPins import RoverPins
class LineFollower():
    _far_left_pin = None
    _left_pin = None
    _right_pin = None
    _far_right_pin = None


    def __init__(self, far_left_pin, left_pin, right_pin, far_right_pin):
        
        self._far_left_pin = far_left_pin
        self._left_pin = left_pin
        self._right_pin = right_pin
        self._far_right_pin = far_right_pin

        #Config GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(RoverPins.BOARD_MODE)

        GPIO.setup(self._far_left_pin, GPIO.IN)
        GPIO.setup(self._left_pin, GPIO.IN)
        GPIO.setup(self._right_pin, GPIO.IN)
        GPIO.setup(self._far_right_pin, GPIO.IN)
        self.read_state()

    def read_state(self):
        self.far_left = GPIO.input(self._far_left_pin)
        self.left = GPIO.input(self._left_pin)
        self.right = GPIO.input(self._right_pin)
        self.far_right = GPIO.input(self._far_right_pin)

    def next_motion(self):
        self.read_state()

        if not self.far_left and not self.left and self.right and self.far_right:   #0011
            return Motion.LEFTFORWARD
        elif not self.far_left and self.left and self.right and self.far_right:    #0111
            return Motion.LEFTROTATE
        elif self.far_left and not self.left and not self.right and self.far_right:     #1001
            return Motion.FORWARD
        elif self.far_left and not self.left and self.right and self.far_right:         #1011
            return Motion.LEFTFORWARD
        elif self.far_left and self.left and not self.right and not self.far_right:     #1100
            return Motion.RIGHTFORWARD
        elif self.far_left and self.left and not self.right and self.far_right:         #1101
            return Motion.RIGHTFORWARD
        elif self.far_left and self.left and self.right and not self.far_right:         #1110
            return Motion.RIGHTROTATE
        elif self.far_left and self.left and self.right and self.far_right:             #1111
            return Motion.STOP
        else:
            # return Stop for any invalid input combination
            return Motion.STOP

