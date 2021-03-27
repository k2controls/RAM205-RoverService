''' Gimbal Class
Implements two Axis gimbal action.
Uses Servo class
'''
from Rover.Servo import Servo

class Gimbal():
    HORIZONTAL_HOME = 90
    VERTICAL_HOME = 90
    h_servo = None
    v_servo = None

    def __init__(self, h_servo: Servo, v_servo: Servo):
        self.h_servo = h_servo
        self.v_servo = v_servo
        self.h_servo.rotate(Gimbal.HORIZONTAL_HOME)
        self.v_servo.rotate(Gimbal.VERTICAL_HOME)
 
    def __del__(self):
        self.h_servo = None
        self.v_servo = None
        
        
