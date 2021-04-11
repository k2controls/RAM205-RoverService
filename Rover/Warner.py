''' Warner Class
Encapsulates a light and buzzer to
create a warning system
'''
from Rover.Buzzer import Buzzer, BuzzerStatus
from Rover.LED import LED, LEDStatus
class Warner():
    
    def __init__(self, led : LED, buzzer : Buzzer):
        self.led = led
        self.buzzer = buzzer
        self.status = "OFF"

    def __str__(self):
        return f"Warner status is {self.status}."
        
    def on(self):
        self.led.on()
        self.buzzer.on()
        self.status = "ON"

    def off(self):
        self.led.off()
        self.buzzer.off()
        self.status = "OFF"

    def alarm_on(self, frequency = 1, duty_cycle = 50):
        self.led.blink(frequency, duty_cycle)
        self.buzzer.beep(frequency, duty_cycle)
        self.status = "ALARM"
    
    def alarm_off(self):
        self.led.off()
        self.buzzer.off()
        self.status = "OFF"

