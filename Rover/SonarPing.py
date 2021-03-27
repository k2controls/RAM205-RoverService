''' Sonar Ping Senor
Service that continually pings and 
provides a distance value as a property
'''

class SonarPing():
    _trigger_pin = None
    _pulse_pin = None
    distance = 0

    def __init__(self, trigger_pin, pulse_pin):
        self._trigger_pin = trigger_pin
        self._pulse_pin = pulse_pin
        #TODO implement sonar ping
        
