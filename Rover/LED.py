''' LED class
Implements LED function including on, off, blink, and dim
PWM port created only if beep() called

'''
import RPi.GPIO as GPIO
from Rover.RoverPins import RoverPins
from enum import Enum

class LEDStatus(Enum):
    OFF = 0
    ON = 1
    BLINK = 2

class LED():
    
    def __init__(self, pin, active_low=False):
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
        return f"LED is {self.status.name}."

    def update(self, status : LEDStatus):
        if status == LEDStatus.OFF.value:
            self.off()
        elif status == LEDStatus.ON.value:
            self.on()
        elif status == LEDStatus.BLINK.value:
            self.blink()
        else:
            raise ValueError("Invalid LED status value.")

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
        self.status = LEDStatus.ON
        self.analog_value = 255

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
        self.status = LEDStatus.OFF
        self.analog_value = 0

    def toggle(self):
        if not self.is_off():
            self.off()
        else:
            self.on()

    def is_on(self):
        return self.status == LEDStatus.ON

    def is_off(self):
        return self.status == LEDStatus.OFF

    def is_blink(self):
        return self.status == LEDStatus.BLINK

    def blink(self, frequency=1, duty_cycle=50):
        self.frequency = frequency
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
        self.status = LEDStatus.BLINK
        self.analog_value = int(duty_cycle/100*255)

    def dim(self, percent_on):
        ''' Specify dim value by entering a value between 0 and 100.
        '''
        if percent_on < 0 or percent_on > 100:
            raise ValueError("LED percent_on must be between 0 and 100.")
        else:
            self.blink(50, percent_on)

    def set_analog(self, analog_value):
        ''' Specify intensity using analog value from min to max.
        '''
        if analog_value < 0 or analog_value > 255:
            raise ValueError("Analog value be between 0 and 255.")
        else:
            self.analog_value = analog_value
            dc = analog_value/255*100
            self.blink(50, dc)
