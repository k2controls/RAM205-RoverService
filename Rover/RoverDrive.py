''' RoverDrive class
Refactored piRover_drive module
Converting module to a Python class

4/11/21
'''
import RPi.GPIO as GPIO
from Rover.RoverPins import RoverPins
from enum import Enum

class DriveMotion(Enum):
    STOP            = (0,0,0,0)
    FORWARD         = (0,1,0,1)
    BACKWARD        = (1,0,1,0)
    LEFTFORWARD     = (0,0,0,1)
    LEFTBACKWARD    = (1,0,0,0)
    LEFTROTATE      = (1,0,0,1)
    RIGHTFORWARD    = (0,1,0,0)
    RIGHTBACKWARD   = (0,0,1,0)
    RIGHTROTATE     = (0,1,1,0)
    
class RoverDrive():

    #constants
    DEFAULT_SPEED = 50
    DELTA_SPEED = 5

    def __init__(self, 
        left_in1_pin, 
        left_in2_pin, 
        leftspeed_pin, 
        right_in1_pin, 
        right_in2_pin, 
        rightspeed_pin):

        self._left_in1_pin = left_in1_pin
        self._left_in2_pin = left_in2_pin
        self._leftspeed_pin = leftspeed_pin
        self._right_in1_pin = right_in1_pin
        self._right_in2_pin = right_in2_pin
        self._rightspeed_pin = rightspeed_pin

        #Configure GPIO settings
        GPIO.setwarnings(False)
        GPIO.setmode(RoverPins.BOARD_MODE)

        #set MC pins as output
        GPIO.setup(self._left_in1_pin, GPIO.OUT, initial = False)
        GPIO.setup(self._left_in2_pin, GPIO.OUT, initial = False)
        GPIO.setup(self._right_in1_pin, GPIO.OUT, initial = False)
        GPIO.setup(self._right_in2_pin, GPIO.OUT, initial = False)
    
        # set enable pins as output
        GPIO.setup(self._leftspeed_pin, GPIO.OUT, initial = True)
        GPIO.setup(self._rightspeed_pin, GPIO.OUT, initial = True)

        self._leftspeed_pwm = GPIO.PWM(self._leftspeed_pin,50)
        self._rightspeed_pwm = GPIO.PWM(self._rightspeed_pin, 50)
        self.speed = RoverDrive.DEFAULT_SPEED
        self._leftspeed_pwm.start(self.speed)
        self._rightspeed_pwm.start(self.speed)

        self.update(DriveMotion.STOP)

    def __del__(self):
        GPIO.cleanup()

    def __str__(self):
        return f"Drive is {self.drive_motion} at a speed of {self.speed}."

    def update(self, drive_motion : DriveMotion):
        self.drive_motion = drive_motion
        GPIO.output(self._left_in1_pin, drive_motion.value[0])
        GPIO.output(self._left_in2_pin, drive_motion.value[1])
        GPIO.output(self._right_in1_pin, drive_motion.value[2])
        GPIO.output(self._right_in2_pin, drive_motion.value[3])

    def set_speed(self, speed):
        if speed < 0 or speed > 100:
            raise ValueError("Invalid speed value.")
        self.speed = speed
        self._leftspeed_pwm.ChangeDutyCycle(self.speed)
        self._rightspeed_pwm.ChangeDutyCycle(self.speed)

    def accelerate(self):
        if self.speed < 100:
            self.speed = self.speed + RoverDrive.DELTA_SPEED
            self._leftspeed_pwm.ChangeDutyCycle(self.speed)
            self._rightspeed_pwm.ChangeDutyCycle(self.speed)

    def decelerate(self):
        if self.speed > 0:
            self.speed = self.speed - RoverDrive.DELTA_SPEED
            self._leftspeed_pwm.ChangeDutyCycle(self.speed)
            self._rightspeed_pwm.ChangeDutyCycle(self.speed)



