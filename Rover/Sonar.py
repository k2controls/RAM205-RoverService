import time
import RPi.GPIO as GPIO
from Rover.RoverPins import RoverPins

class Sonar(object):
    """A wrapper class for servo ping sensor"""
    INVALID_DISTANCE = -1

    def __init__(self, trigger_pin, echo_pin, sample_freq=5, duty_cyle=1):
        self.trigger_pin =  trigger_pin
        self.echo_pin = echo_pin
        self.sample_freq = sample_freq
        self.duty_cyle = duty_cyle
        self._t1 = 0
        self._t2 = 0
        self.distance = 0
        
        GPIO.setwarnings(False)
        GPIO.setmode(RoverPins.BOARD_MODE)

        GPIO.setup(self.trigger_pin, GPIO.OUT)
        self.trigger = GPIO.PWM(self.trigger_pin, self.sample_freq)
        self.trigger.start(self.duty_cyle) 

        GPIO.setup(self.echo_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.echo_pin, GPIO.BOTH, callback=self._sonar_event_handler)

    def __str__(self):
        return f"Sonar: d={self.distance}."
        
    def _sonar_event_handler(self, channel):
        if self._t1 == self._t2:
            self._t1 = time.time()
        else:
            self._t2 = time.time()
            self.distance = (self._t2-self.t1) * 340 / 2
            self._t1 = self._t2


