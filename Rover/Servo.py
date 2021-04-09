
''' Servo Class
Implements basic servo action
'''
import RPi.GPIO as GPIO 
from Rover.RoverPins import RoverPins

class Servo():
    _FREQ = 50
    _PERIOD = 1/_FREQ

    _pin = None
    min_position_value = 0
    max_position_value = 180

    def __init__(self, pin, 
            min_position_value = 0, 
            max_position_value = 180, 
            min_pulse_width=.001, 
            max_pulse_width=.002):

        self._pin = pin
        self.min_position_value = min_position_value
        self.max_position_value = max_position_value
        self.min_duty_cycle = min_pulse_width/self._PERIOD * 100
        self.max_duty_cycle = max_pulse_width/self._PERIOD * 100
        self.mid_duty_cycle = (self.min_duty_cycle + self.max_duty_cycle)/2
        self.duty_cycle = self.mid_duty_cycle
        self.pulse_width = self.duty_cycle/100 * self._PERIOD

        GPIO.setmode(RoverPins.BOARD_MODE)
        GPIO.setwarnings(False)
        GPIO.setup(self._pin, GPIO.OUT)
        self._pwm = GPIO.PWM(self._pin, self._FREQ)
        self._pwm.start(self.duty_cycle)

    def __del__(self):
        GPIO.cleanup()

    def rotate(self, position):
        if position < self.min_position_value or position > self.max_position_value:
            raise ValueError("ERROR: That is not a valid serve position.")
        else:
            percent_position = position/(self.max_position_value - self.min_position_value)
            delta_dc = percent_position * (self.max_duty_cycle-self.min_duty_cycle)
            offset_dc = self.min_duty_cycle
            self.duty_cycle = offset_dc + delta_dc
            self.pulse_width = self.duty_cycle/100 * self._PERIOD
            self._pwm.ChangeDutyCycle(self.duty_cycle)



    
