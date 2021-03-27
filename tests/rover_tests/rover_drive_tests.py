from Rover.RoverDrive import Motion

def do_tests(rover):
    test_count = 0

    drive = rover.rover_drive

    print("Testing Rover Drive.")
    print()
    input("PREPARE ROVER FOR MOTION! Press enter to continue.")
    print()
    input("Rover is stopped. Press Enter to move FORWARD.")
    drive.update(Motion.FORWARD)
    if input("Is drive moving FORWARD? ").lower()[0]=="y":
        test_count +=1
        drive.update(Motion.STOP)
    else:
        drive.update(Motion.STOP)
        return 0

    input("Rover is stopped. Press Enter to move BACKWARD.")
    drive.update(Motion.BACKWARD)
    if input("Is drive moving BACKWARD? ").lower()[0]=="y":
        test_count +=1
        drive.update(Motion.STOP)
    else:
        drive.update(Motion.STOP)
        return 0

    input("Rover is stopped. Press Enter to move LEFTFORWARD.")
    drive.update(Motion.LEFTFORWARD)
    if input("Is drive moving LEFTFORWARD? ").lower()[0]=="y":
        test_count +=1
        drive.update(Motion.STOP)
    else:
        drive.update(Motion.STOP)
        return 0

    input("Rover is stopped. Press Enter to move LEFTBACKWARD.")
    drive.update(Motion.LEFTBACKWARD)
    if input("Is drive moving LEFTBACKWARD? ").lower()[0]=="y":
        test_count +=1
        drive.update(Motion.STOP)
    else:
        drive.update(Motion.STOP)
        return 0

    input("Rover is stopped. Press Enter to move LEFTROTATE.")
    drive.update(Motion.LEFTROTATE)
    if input("Is drive moving LEFTROTATE? ").lower()[0]=="y":
        test_count +=1
        drive.update(Motion.STOP)
    else:
        drive.update(Motion.STOP)
        return 0


    input("Rover is stopped. Press Enter to move RIGHTFORWARD.")
    drive.update(Motion.RIGHTFORWARD)
    if input("Is drive moving RIGHTFORWARD? ").lower()[0]=="y":
        test_count +=1
        drive.update(Motion.STOP)
    else:
        drive.update(Motion.STOP)
        return 0

    input("Rover is stopped. Press Enter to move RIGHTBACKWARD.")
    drive.update(Motion.RIGHTBACKWARD)
    if input("Is drive moving RIGHTBACKWARD? ").lower()[0]=="y":
        test_count +=1
        drive.update(Motion.STOP)
    else:
        drive.update(Motion.STOP)
        return 0

    input("Rover is stopped. Press Enter to move RIGHTROTATE.")
    drive.update(Motion.RIGHTROTATE)
    if input("Is drive moving RIGHTROTATE? ").lower()[0]=="y":
        test_count +=1
        drive.update(Motion.STOP)
    else:
        drive.update(Motion.STOP)
        return 0

    drive.update(Motion.STOP)

    return test_count
