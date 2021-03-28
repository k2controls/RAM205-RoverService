''' Call make_rover() to construct Rover object 
along with child objects
'''
from Rover.Rover import Rover
from Rover.Buzzer import Buzzer
from Rover.Camera import Camera
from Rover.Gimbal import Gimbal
from Rover.LED import LED
from Rover.LineFollower import LineFollower
from Rover.RGBLed import RGBLed
from Rover.RoverDrive import RoverDrive
from Rover.RoverPins import RoverPins
from Rover.Servo import Servo
from Rover.SonarPing import SonarPing
from Rover.Warner import Warner

def make_rover():
    rover = Rover()

    buzzer = Buzzer(RoverPins.BUZZER_PIN)
    rover.buzzer = buzzer

    camera = Camera()
    rover.camera = camera

    g_h_servo = Servo(RoverPins.SERVO_HEADER_2)
    g_v_servo = Servo(RoverPins.SERVO_HEADER_3)
    gimbal = Gimbal(g_h_servo,g_v_servo)
    rover.gimbal = gimbal
 
    #TODO do rgb_led on your own
    r_led = LED(RoverPins.LED_RED_PIN)
    g_led = LED(RoverPins.LED_GREEN_PIN)
    b_led = LED(RoverPins.LED_BLUE_PIN)
    rgb_led = RGBLed(r_led, g_led, b_led)
    rover.rgb_led = rgb_led

    lf = LineFollower(
        RoverPins.LINE_FOLLOWER_L2_PIN,
        RoverPins.LINE_FOLLOWER_L1_PIN,
        RoverPins.LINE_FOLLOWER_R1_PIN,
        RoverPins.LINE_FOLLOWER_R2_PIN
    )
    rover.line_follower = lf

    rd = RoverDrive(
        RoverPins.DRIVE_LEFT_IN1_PIN,
        RoverPins.DRIVE_LEFT_IN2_PIN,
        RoverPins.DRIVE_LEFT_EN_PIN,
        RoverPins.DRIVE_RIGHT_IN1_PIN,
        RoverPins.DRIVE_RIGHT_IN2_PIN,
        RoverPins.DRIVE_RIGHT_EN_PIN
    )
    rover.rover_drive = rd

    s = Servo(RoverPins.SERVO_HEADER_1)
    rover.servo = s

    ping = SonarPing(RoverPins.PING_TRIGGER_PIN, RoverPins.PING_PULSE_PIN)
    rover.sonar_ping = ping

    led = LED(RoverPins.SERVO_HEADER_4)
    w = Warner(led, buzzer)
    rover.warner = w

    return rover


