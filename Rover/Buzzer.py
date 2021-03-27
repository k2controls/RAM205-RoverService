''' Buzzer Class
Implements buzzer function including on, off, beep
PWM port created only if beep() called

'''
import RPi.GPIO as GPIO

class Buzzer():
    pin = None
    _pwm = None
    _duty_cycle = None

    def __init__(self, pin, active_low=True):
        self.pin = pin
        self.active_low = active_low

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.pin, GPIO.OUT)
        
        self.off()

    def __del__(self):
        GPIO.cleanup()

    def update(self, state):
        if state:
            self.on()
        else:
            self.off()
            
    def on(self):
        if self._pwm:
            if self.active_low:
                self._duty_cycle = 0
            else:
                self._duty_cycle = 100
            self._pwm.ChangeDutyCycle(self._duty_cycle)
        else:
            if self.active_low:
                GPIO.output(self.pin, False)
            else:
                GPIO.output(self.pin, True) 

    def off(self):
        if self._pwm:
            if self.active_low:
                self._duty_cycle = 100
            else:
                self._duty_cycle = 0
            self._pwm.ChangeDutyCycle(self._duty_cycle)
        else:
            if self.active_low:
                GPIO.output(self.pin, True)
            else:
                GPIO.output(self.pin, False) 

    def toggle(self):
        if self.is_on():
            self.off()
        else:
            self.on()

    def is_on(self):
        if self._pwm:   #pwm active then port is "on" only at DC = 100
            return self._duty_cycle == 100
        elif self.active_low:
            return not GPIO.input(self.pin)
        else:
            return GPIO.input(self.pin)

    def is_off(self):
        if self._pwm:   #pwm active then port is "off" only at DC = 0
            return self._duty_cycle == 0
        else:
            return not self.is_on()

    def beep(self, frequency=1, duty_cycle=50):
        if self.active_low:
            self._duty_cycle = 100 - duty_cycle
        else:
            self._duty_cycle = duty_cycle

        if self._pwm == None:
            self._pwm = GPIO.PWM(self.pin, frequency)
            self._pwm.start(self._duty_cycle)
        else:
            self._pwm.ChangeFrequency(frequency)
            self._pwm.ChangeDutyCycle(self._duty_cycle)

