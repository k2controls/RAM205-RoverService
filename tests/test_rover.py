from tests.rover_tests.test_buzzer import test_buzzer
from tests.rover_tests.test_camera import test_camera
from tests.rover_tests.test_gimbal import test_gimbal
from tests.rover_tests.test_led import test_led
from tests.rover_tests.test_line_follower import test_line_follower
from tests.rover_tests.test_rgb_led import test_rgb_led
from tests.rover_tests.test_rover_drive import test_rover_drive
from tests.rover_tests.test_servo import test_servo
from tests.rover_tests.test_sonar_ping import test_sonar_ping
from tests.rover_tests.test_warner import test_warner
from Rover.rover_factory import make_rover

def test_rover(rover):
    if not test_buzzer(rover):
        print("Buzzer tests failed.")
    elif not test_camera(rover):
        print("Camera tests failed.")
    elif not test_gimbal(rover):
        print("Gimbal tests failed.")
    elif not test_led(rover):
        print("LED tests failed.")
    elif not test_rgb_led(rover):
        print("RGB LED tests failed.")
    elif not test_rover_drive(rover):
        print("Rover drive tests failed.")
    elif not test_servo(rover):
        print("Servo tests failed.")
    elif not test_sonar_ping(rover):
        print("Sonar ping tests failed.")
    elif not test_warner(rover):
        print("warner tests failed.")
    else:
        if input("Test Line Follower inputs? ").lower()[0]=="y":
            if not test_line_follower(rover):
                print("Line Follower test failed.")
            else:
                print("All tests passed!")
        else:
            print("All tests passed!")

def do_tests():
    print("This is a test of the rover unit. Components will be activated")
    print("and you will be asked to verify by entering either Y or N.")
    entry = int(input("Enter 1 to start Rover testing. Enter 0 to skip. "))
    if entry:
        print()
        print("Testing Rover...")
        rover = make_rover()
        test_rover(rover)
        print("Rover test complete.")
    print()    