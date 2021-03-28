
def test_servo(rover):
    test_count = 0

    print("Testing front servo.")

    # test horizontal
    servo = rover.servo

    servo.rotate(0)
    if input("Is front servo fully counter-clockwise? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0
    
    servo.rotate(90)
    if input("Is front servo centered? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    servo.rotate(180)
    if input("Is front servo fully clockwise? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    servo.rotate(90)

    return test_count
