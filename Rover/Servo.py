
''' Servo Class
Implements basic servo action
'''
import RPi.GPIO as GPIO 
from Rover.RoverPins import RoverPins
class Servo():
    FREQ = 50
    PERIOD = 1/FREQ

    def __init__(self, pin, 
            min_position_value = 0, 
            max_position_value = 180, 
            min_pulse_width=.001, 
            max_pulse_width=.002):

        self.pin = pin
        self.min_position_value = min_position_value
        self.max_position_value = max_position_value
        self.min_duty_cycle = min_pulse_width/Servo.PERIOD * 100
        self.max_duty_cycle = max_pulse_width/Servo.PERIOD * 100
        self.mid_duty_cycle = (self.min_duty_cycle + self.max_duty_cycle)/2

        GPIO.setmode(RoverPins.BOARD_MODE)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, Servo.FREQ)
        self.pwm.start(self.mid_duty_cycle)
        #center
        self.rotate((self.max_position_value - self.min_position_value)/2)

    def __del__(self):
        GPIO.cleanup()

    def __str__(self):
        return f"Servo is a position {self.position} ({self.percent_position}%)."
        
    def rotate(self, position):
        if position < self.min_position_value or position > self.max_position_value:
            raise ValueError("ERROR: That is not a valid servo position.")
        else:
            self.position = position
            self.percent_position = position/(self.max_position_value - self.min_position_value)
            delta_dc = self.percent_position * (self.max_duty_cycle-self.min_duty_cycle)
            offset_dc = self.min_duty_cycle
            self.duty_cycle = offset_dc + delta_dc
            self.pulse_width = self.duty_cycle/100 * Servo.PERIOD
            self.pwm.ChangeDutyCycle(self.duty_cycle)



    
