''' Warner Class
Encapsulates a light and buzzer to
create a warning system
'''
import RPi.GPIO as GPIO
import time

#LED_PIN = 19
#BUZZER_PIN = 24

class Warner():
    led = None
    buzzer = None

    def __init__(self, led, buzzer):
        self.led = led
        self.buzzer = buzzer

    def on(self):
        self.led.on()
        self.buzzer.on()
    
    def off(self):
        self.led.off()
        self.buzzer.off()

    def alarm_on(self, frequency, duty_cycle):
        self.led.blink(frequency, duty_cycle)
        self.buzzer.beep(frequency, duty_cycle)
    
    def alarm_off(self):
        self.led.blink(1, 0)
        self.buzzer.beep(1, 0)


