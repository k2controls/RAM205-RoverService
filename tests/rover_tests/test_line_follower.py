from Rover.RoverDrive import Motion

def test_line_follower(rover):
    test_count = 0
    lf = rover.line_follower

    print("Testing Line Follower")
    print()
    print("Calibrate line follower.")
    print()
    input("No line is under sensor and sensor are off. Press Enter to validate.")
    lf.read_state()
    if lf.far_left and lf.left and lf.right and lf.far_right:
        print("State verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    input("Position line under far_left only. Press Enter to validate.")
    lf.read_state()
    if not lf.far_left and lf.left and lf.right and lf.far_right:
        print("State verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    input("Position line under left only. Press Enter to validate.")
    lf.read_state()
    if lf.far_left and not lf.left and lf.right and lf.far_right:
        print("State verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    input("Position line under right only. Press Enter to validate.")
    lf.read_state()
    if lf.far_left and lf.left and not lf.right and lf.far_right:
        print("State verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    input("Position line under far right only. Press Enter to validate.")
    lf.read_state()
    if lf.far_left and lf.left and lf.right and not lf.far_right:
        print("State verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    
    print("Testing line follower next_motion()")
    print("No line is under sensors, sensors are off")
    input("Next motion is STOP. Press Enter to validate.")
    if lf.next_motion()== Motion.STOP:
        print("Next motion verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    print("Position line under far_left only.")
    input("Next motion is LEFTROTATE. Press Enter to validate.")
    if lf.next_motion()== Motion.LEFTROTATE:
        print("Next motion verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    print("Position line under far_left and left.")
    input("Next motion is LEFTFORWARD. Press Enter to validate.")
    if lf.next_motion()== Motion.LEFTFORWARD:
        print("Next motion verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    print("Position line under far_left only.")
    input("Next motion is LEFTROTATE. Press Enter to validate.")
    if lf.next_motion()== Motion.LEFTFORWARD:
        print("Next motion verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    print("Position line under left and right.")
    input("Next motion is FORWARD. Press Enter to validate.")
    if lf.next_motion()== Motion.FORWARD:
        print("Next motion verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    print("Position line under right only.")
    input("Next motion is RIGHTROTATE. Press Enter to validate.")
    if lf.next_motion()== Motion.RIGHTFORWARD:
        print("Next motion verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    print("Position line under right and far_right only.")
    input("Next motion is RIGHTROTATE. Press Enter to validate.")
    if lf.next_motion()== Motion.RIGHTFORWARD:
        print("Next motion verified. Test passed")
        test_count +=1
    else:
        return 0

    print()
    print("Position line under far_right only.")
    input("Next motion is RIGHTROTATE. Press Enter to validate.")
    if lf.next_motion()== Motion.RIGHTROTATE:
        print("Next motion verified. Test passed")
        test_count +=1
    else:
        return 0

    return test_count
