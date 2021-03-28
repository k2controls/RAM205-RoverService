from Rover.RGBLed import LED_COLOR

def test_rgb_led(rover):
    test_count = 0

    print("Testing RGB LED.")
    rover.rgb_led.set_color(LED_COLOR.RED)
    if input("Is RGB LED red? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    rover.rgb_led.set_color(LED_COLOR.GREEN)
    if input("Is RGB LED green? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0
    
    rover.rgb_led.set_color(LED_COLOR.BLUE)
    if input("Is RGB LED blue? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    rover.rgb_led.set_color(LED_COLOR.AMBER)
    if input("Is RGB LED amber? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    rover.rgb_led.set_color(LED_COLOR.CYAN)
    if input("Is RGB LED cyan? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    rover.rgb_led.set_color(LED_COLOR.MAGENTA)
    if input("Is RGB LED magenta? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    rover.rgb_led.set_color(LED_COLOR.WHITE)
    if input("Is RGB LED white? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    rover.rgb_led.set_color(LED_COLOR.OFF)
    if input("Is RGB LED off? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    return test_count
