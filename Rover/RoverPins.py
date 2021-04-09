''' Rover Pins Class
Data class containing pin number definitions.

- 3/17/21   Added trigger and pulse pins for ping sensor
- 4/9/21 Added GPIO vs Pin # option
'''
import RPi.GPIO as GPIO

class RoverPins():
    BOARD_MODE = GPIO.BCM
    #BOARD_MODE = GPIO.BOARD
    if BOARD_MODE == GPIO.BOARD:
        BUZZER_PIN = 24
        LED_RED_PIN = 15
        LED_GREEN_PIN = 13
        LED_BLUE_PIN = 18
        LINE_FOLLOWER_L2_PIN = 5
        LINE_FOLLOWER_L1_PIN = 29
        LINE_FOLLOWER_R1_PIN = 7
        LINE_FOLLOWER_R2_PIN = 12
        DRIVE_LEFT_IN1_PIN = 40
        DRIVE_LEFT_IN2_PIN = 38
        DRIVE_LEFT_EN_PIN = 36
        DRIVE_RIGHT_IN1_PIN = 37
        DRIVE_RIGHT_IN2_PIN = 35
        DRIVE_RIGHT_EN_PIN = 33
        SERVO_HEADER_1 = 16
        SERVO_HEADER_2 = 23
        SERVO_HEADER_3 = 21
        SERVO_HEADER_4 = 19
        SERVO_HEADER_5 = 22
        SERVO_HEADER_6 = 3
        #added 3/17
        PING_TRIGGER_PIN = 28
        PING_PULSE_PIN = 27
        
    elif BOARD_MODE == GPIO.BCM:
        BUZZER_PIN = 8
        LED_RED_PIN = 22
        LED_GREEN_PIN = 27
        LED_BLUE_PIN = 24
        LINE_FOLLOWER_L2_PIN = 3
        LINE_FOLLOWER_L1_PIN = 5
        LINE_FOLLOWER_R1_PIN = 4
        LINE_FOLLOWER_R2_PIN = 18
        DRIVE_LEFT_IN1_PIN = 21
        DRIVE_LEFT_IN2_PIN = 22
        DRIVE_LEFT_EN_PIN = 16
        DRIVE_RIGHT_IN1_PIN = 26
        DRIVE_RIGHT_IN2_PIN = 19
        DRIVE_RIGHT_EN_PIN = 13
        SERVO_HEADER_1 = 23
        SERVO_HEADER_2 = 11
        SERVO_HEADER_3 = 9
        SERVO_HEADER_4 = 10
        SERVO_HEADER_5 = 25
        SERVO_HEADER_6 = 2
        #added 3/17
        PING_TRIGGER_PIN = 0
        PING_PULSE_PIN = 1
    
