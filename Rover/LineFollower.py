''' Line Follower class
Senses line follower inputs and define
next drive motion
'''
#from Rover import RoverDrive
from Rover.RoverDrive import DriveMotion
from Rover.RoverPins import RoverPins
import RPi.GPIO as GPIO

class LineFollower():

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

    def __str__(self):
        next = self.next_motion()
        s = f"Line follower status: {self.state}, Next motion: {next}."
        return s

    def read_state(self):
        ''' Read state return tuple with logic 1 indicated line is sensed. 
        (sensor is active low.)
        example: (0110) - line is centered, move forward
        '''
        self.far_left = not GPIO.input(self._far_left_pin)
        self.left = not GPIO.input(self._left_pin)
        self.right = not GPIO.input(self._right_pin)
        self.far_right = not GPIO.input(self._far_right_pin)
        
        return ({self.far_left},{self.left},{self.right},{self.far_right})

    def next_motion(self):
        next = DriveMotion.STOP
        state = self.read_state()
        
        if state == (0,1,1,0):
            next = DriveMotion.FORWARD    
        elif state == (0,1,0,0) or state == (1,1,0,0):
            next = DriveMotion.LEFTFORWARD
        elif state == (1,0,0,0):
            next = DriveMotion.LEFTROTATE
        elif state == (0,0,1,0) or state == (0,0,1,1):
            next = DriveMotion.RIGHTFORWARD
        elif state == (0,0,0,1):
            next = DriveMotion.RIGHTROTATE
        
        return next
