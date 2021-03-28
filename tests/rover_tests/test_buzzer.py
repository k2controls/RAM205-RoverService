
def test_buzzer(rover):
    test_count = 0

    print("Testing buzzer.")
    rover.buzzer.on()
    if input("Is buzzer on? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    rover.buzzer.off()
    if input("Is buzzer off? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0
    
    rover.buzzer.toggle()
    if input("Did buzzer toggle on? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    if rover.buzzer.is_on():
        test_count +=1
    else:
        return 0

    if not rover.buzzer.is_off():
        test_count +=1
    else:
        return 0
    
    rover.buzzer.toggle()
    if input("Did buzzer toggle off? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    if not rover.buzzer.is_on():
        test_count +=1
    else:
        return 0

    if rover.buzzer.is_off():
        test_count +=1
    else:
        return 0

    rover.buzzer.beep(.5,30)
    if input("Is buzzer short beeping at 2 sec period? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    rover.buzzer.off()

    return test_count

