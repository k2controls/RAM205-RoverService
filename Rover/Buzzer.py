''' Buzzer Class
Implements buzzer function including on, off, beep
PWM port created only if beep() called
'''
import RPi.GPIO as GPIO
from Rover.RoverPins import RoverPins
from enum import Enum

class BuzzerStatus(Enum):
        OFF = 0
        ON = 1
        BEEP = 2

class Buzzer():
    
    def __init__(self, pin, active_low=True):
        self.pin = pin
        self.active_low = active_low
        self.pwm = None

        GPIO.setwarnings(False)
        GPIO.setmode(RoverPins.BOARD_MODE)
        GPIO.setup(self.pin, GPIO.OUT)
        
        self.off()

    def __del__(self):
        GPIO.cleanup()

    def __str__(self):
        return f"Buzzer is {self.status.name}."

    def update(self, status: BuzzerStatus):
        if status == BuzzerStatus.OFF.value:
            self.off()
        elif status == BuzzerStatus.ON.value:
            self.on()
        elif status == BuzzerStatus.BEEP.value:
            self.beep()
        else:
            raise ValueError("Invalid Buzzer status value.")

    def on(self):
        if self.pwm:
            if self.active_low:
                self.duty_cycle = 0
            else:
                self.duty_cycle = 100
            self.pwm.ChangeDutyCycle(self.duty_cycle)
        else:
            if self.active_low:
                GPIO.output(self.pin, False)
            else:
                GPIO.output(self.pin, True) 
        self.status = BuzzerStatus.ON
  
    def off(self):
        if self.pwm:
            if self.active_low:
                self.duty_cycle = 100
            else:
                self.duty_cycle = 0
            self.pwm.ChangeDutyCycle(self.duty_cycle)
        else:
            if self.active_low:
                GPIO.output(self.pin, True)
            else:
                GPIO.output(self.pin, False) 
        self.status = BuzzerStatus.OFF
  
    def toggle(self):
        if not self.is_off():
            self.off()
        else:
            self.on()

    def is_on(self):
        return self.status == BuzzerStatus.ON

    def is_off(self):
        return self.status == BuzzerStatus.OFF

    def is_beep(self):
        return self.status == BuzzerStatus.BEEP

    def beep(self, frequency=1, duty_cycle=50):
        if self.active_low:
            self.duty_cycle = 100 - duty_cycle
        else:
            self.duty_cycle = duty_cycle

        if self.pwm == None:
            self.pwm = GPIO.PWM(self.pin, frequency)
            self.pwm.start(self.duty_cycle)
        else:
            self.pwm.ChangeFrequency(frequency)
            self.pwm.ChangeDutyCycle(self.duty_cycle)
        self.status = BuzzerStatus.BEEP
