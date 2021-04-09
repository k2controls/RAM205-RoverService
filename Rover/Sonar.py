import time
import queue
import RPi.GPIO as GPIO
from Rover.RoverPins import RoverPins

class Sonar(object):
    """A wrapper class for servo ping sensor"""
    INVALID_DISTANCE = -1

    def __init__(self, trigger_pin, echo_pin, sample_freq=1):
        self.trigger_pin =  trigger_pin
        self.echo_pin = echo_pin
        self.sample_freq = sample_freq
        self._t1 = 0
        self.d = self.INVALID_DISTANCE
        self.distance_stack = queue.LifoQueue(10)

        GPIO.setwarnings(False)
        GPIO.setmode(RoverPins.BOARD_MODE)

        GPIO.setup(self.trigger_pin, GPIO.OUT)
        self.trigger = GPIO.PWM(self.trigger_pin, self.sample_freq)
        self.trigger.start(5)  #5% duty cycle for trigger pulse

        GPIO.setup(self.echo_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.echo_pin, GPIO.BOTH, callback=self._sonar_event_handler)

    def _sonar_event_handler(self, channel):
        if GPIO.input(self.echo_pin): 
            self._t1 = time.time()
        else:
            delta_time = time.time() - self._t1
            self.d = delta_time * 340 / 2
            # if self.d < .002 or self.d > 5:
            #     #out of range - return None
            #     self.distance_stack.put(None)
            # else:
            #     self.distance_stack.put(self.d)

   
    def distance(self):
        if self.distance_stack.empty():
            return None
        else:
            return self.distance_stack.get()


