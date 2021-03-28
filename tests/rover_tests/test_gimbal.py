
def test_gimbal(rover):
    test_count = 0

    print("Testing gimbal.")
    # test horizontal
    servo = rover.gimbal.h_servo

    servo.rotate(0)
    if input("Is horizontal camera servo fully counter-clockwise? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0
    
    servo.rotate(90)
    if input("Is horizontal camera servo centered? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    servo.rotate(180)
    if input("Is horizontal camera servo fully clockwise? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    # test vertical
    servo = rover.gimbal.v_servo

    servo.rotate(0)
    if input("Is vertical camera servo fully counter-clockwise? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0
    
    servo.rotate(90)
    if input("Is vertical camera servo centered? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    servo.rotate(180)
    if input("Is vertical camera servo fully clockwise? ").lower()[0]=="y":
        test_count +=1
    else:
        return 0

    return test_count

