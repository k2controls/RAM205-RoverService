from Rover.RoverDrive import DriveMotion

drive = None

def test_drive_motion(drive_motion : DriveMotion):
    returnVal = 1
    try:
        print()
        input(f"Rover is stopped. Press Enter to move {drive_motion.name}.")
        drive.update(drive_motion)
        if input(f"Is drive moving {drive_motion.name}? ").lower()[0]!="y":
            returnVal = 0
        drive.update(DriveMotion.STOP)
    except:
        print(f"{drive_motion} test failed due to exception.")
        returnVal = 0
        drive.update(DriveMotion.STOP)
    finally:
        return returnVal

def test_rover_drive(rover):
    global drive
    drive = rover.rover_drive
    test_count = 0

    print("Testing Rover Drive.")
    print()
    input("PREPARE ROVER FOR MOTION! Press enter to continue.")
    print()
    if not test_drive_motion(DriveMotion.FORWARD):
        return 0
    test_count +=1
    
    if not test_drive_motion(DriveMotion.BACKWARD):
        return 0
    test_count +=1
    
    if not test_drive_motion(DriveMotion.LEFTFORWARD):
        return 0
    test_count +=1
    
    if not test_drive_motion(DriveMotion.LEFTBACKWARD):
        return 0
    test_count +=1
    
    if not test_drive_motion(DriveMotion.LEFTROTATE):
        return 0
    test_count +=1
    
    if not test_drive_motion(DriveMotion.RIGHTFORWARD):
        return 0
    test_count +=1
    
    if not test_drive_motion(DriveMotion.RIGHTBACKWARD):
        return 0
    test_count +=1
    
    if not test_drive_motion(DriveMotion.RIGHTROTATE):
        return 0
    test_count +=1

    drive.update(DriveMotion.STOP)

    return test_count
