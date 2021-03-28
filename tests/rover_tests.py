from rover_tests import *

def rover_tests(rover):
    if not buzzer_tests(rover):
        print("buzzer tests failed.")
    elif not camera_tests(rover):
        print("camera tests failed.")
    elif not gimbal_tests(rover):
        print("gimbal tests failed.")
    elif not led_tests(rover):
        print("LED tests failed.")
    elif not line_follower_tests(rover):
        print("line follower tests failed.")
    elif not rover_drive_tests(rover):
        print("Rover drive tests failed.")
    elif not rover_sonar_ping_tests(rover):
        print("camera tests failed.")
    elif not rover_warner_tests(rover):
        print("camera tests failed.")
    else:
        print("All tests passed!")

