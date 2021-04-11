from Rover.Warner import Warner, LEDStatus, BuzzerStatus

w = None

def test_on():
    print()
    print("Testing warner on...")
    w.on()
    if w.status == "ON" and w.led.status == LEDStatus.ON and w.buzzer.status == BuzzerStatus.ON:
        print("Warner on passed.")
        return 1
    else:
        print("Warner on failed.")
        return 0
  
def test_off():
    print()
    print("Testing warner off...")
    w.off()
    if w.status == "OFF" and w.led.status == LEDStatus.OFF and w.buzzer.status == BuzzerStatus.OFF:
        print("Warner on passed.")
        return 1
    else:
        print("Warner on failed.")
        return 0
  
def test_alarm_on():
    print()
    print("Testing warner alarm on...")
    w.alarm_on()
    if w.status == "ALARM" and w.led.status == LEDStatus.BLINK and w.buzzer.status == BuzzerStatus.BEEP:
        print("Warner alarm on passed.")
        return 1
    else:
        print("Warner alarm off failed.")
        return 0

def test_alarm_off():
    print()
    print("Testing warner alarm off...")
    w.alarm_off()
    if w.status == "OFF" and w.led.status == LEDStatus.OFF and w.buzzer.status == BuzzerStatus.OFF:
        print("Warner alarm off passed.")
        return 1
    else:
        print("Warner alarm off failed.")
        return 0

def test_warner(rover):
    global w
    w = rover.warner

    print()
    print("Testing warner.")
    if not test_on():
        return 0
    if not test_off():
        return 0
    if not test_alarm_on():
        return 0
    if not test_alarm_off():
        return 0
    return 1