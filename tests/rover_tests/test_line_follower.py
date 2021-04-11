from Rover.RoverDrive import DriveMotion

line_follower = None

def test_state(message, state):
    print()
    print(message)
    input()
    s = line_follower.read_state()
    if s == state:
        print("State verified. Test passed")
        return 1
    else:
        print(f"Invalid state {s}. Expected {state}. Test failed.")
        return 0

def test_next_motion(message, next_motion : DriveMotion):
    print()
    print(message)
    input()
    n = line_follower.next_motion()
    if n == next_motion:
        print("Next motion verified. Test passed")
        return 1
    else:
        print(f"Invalid next motion {n}. Expected {next_motion}. Test failed.")
        return 0

def test_line_follower(rover):
    global line_follower
    line_follower = rover.line_follower
    test_count = 0
    print("Testing Line Follower")
    print()
    print("Calibrate line follower prior to testing.")
    print()
    m ="No line is under sensor and sensor are off. Press Enter to validate."
    if not test_state(m, (0,0,0,0)):
        return 0

    m = "Position line under far_left only. Press Enter to validate."
    if not test_state(m, (1,0,0,0)):
        return 0

    m = "Position line under left only. Press Enter to validate."
    if not test_state(m, (0,1,0,0)):
        return 0

    m = "Position line under right only. Press Enter to validate."
    if not test_state(m, (0,0,1,0)):
        return 0

    m = "Position line under far_right only. Press Enter to validate."
    if not test_state(m, (0,0,0,1)):
        return 0

    print()
    print("Testing line follower next_motion()")

    m ="No line is under sensors. Sensors are off. Next motion is STOP."
    if not test_next_motion(m, DriveMotion.STOP):
        return 0

    m = "Position line under far_left only. Next motion is LEFTROTATE."
    if not test_next_motion(m, DriveMotion.LEFTROTATE):
        return 0

    m = "Position line under far_left and left. Next motion is LEFTFORWARD."
    if not test_next_motion(m, DriveMotion.LEFTFORWARD):
        return 0

    m = "Position line under left only. Next motion is LEFTFORWARD."
    if not test_next_motion(m, DriveMotion.LEFTFORWARD):
        return 0

    m = "Position line under left and right. Next motion is FORWARD"
    if not test_next_motion(m, DriveMotion.FORWARD):
        return 0

    m = "Position line under right only. Next motion is RIGHTFORWARD."
    if not test_next_motion(m, DriveMotion.RIGHTFORWARD):
        return 0

    m = "Position line under right and far_right. Next motion is RIGHTFORWARD"
    if not test_next_motion(m, DriveMotion.RIGHTFORWARD):
        return 0

    m = "Position line under far_right only. Next motion is RIGHTROTATE."
    if not test_next_motion(m, DriveMotion.RIGHTROTATE):
        return 0

    return 1
