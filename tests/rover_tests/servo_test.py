from Rover.Servo import Servo

#test default constructor
s = Servo(16)
print(f"Duty cycle = {s.duty_cycle}")
print(f"Pulse width = {s.pulse_width}")
pos = 0
s.rotate(pos)
print(f"Position = {pos}")
print(f"Duty cycle = {s.duty_cycle}")
print(f"Pulse width = {s.pulse_width}")
pos = 180
s.rotate(pos)
print(f"Position = {pos}")
print(f"Duty cycle = {s.duty_cycle}")
print(f"Pulse width = {s.pulse_width}")
pos = 90
s.rotate(pos)
print(f"Position = {pos}")
print(f"Duty cycle = {s.duty_cycle}")
print(f"Pulse width = {s.pulse_width}")


#test constructor with min and max position
s = Servo(16, 0, 1)
print(f"Duty cycle = {s.duty_cycle}")
print(f"Pulse width = {s.pulse_width}")
pos = 0
s.rotate(pos)
print(f"Position = {pos}")
print(f"Duty cycle = {s.duty_cycle}")
print(f"Pulse width = {s.pulse_width}")
pos = 1
s.rotate(pos)
print(f"Position = {pos}")
print(f"Duty cycle = {s.duty_cycle}")
print(f"Pulse width = {s.pulse_width}")
pos = .5
s.rotate(pos)
print(f"Position = {pos}")
print(f"Duty cycle = {s.duty_cycle}")
print(f"Pulse width = {s.pulse_width}")

#test constructor with min and max pulse width
s = Servo(16, min_pulse_width=.0005, max_pulse_width=.0025)
print(f"Duty cycle = {s.duty_cycle}")
print(f"Pulse width = {s.pulse_width}")
pos = 0
s.rotate(pos)
print(f"Position = {pos}")
print(f"Duty cycle = {s.duty_cycle}")
print(f"Pulse width = {s.pulse_width}")
pos = 180
s.rotate(pos)
print(f"Position = {pos}")
print(f"Duty cycle = {s.duty_cycle}")
print(f"Pulse width = {s.pulse_width}")
pos = 90
s.rotate(pos)
print(f"Position = {pos}")
print(f"Duty cycle = {s.duty_cycle}")
print(f"Pulse width = {s.pulse_width}")