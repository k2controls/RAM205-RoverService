''' Rover Pins Class
Data class containing pin number definitions.

- 3/17/21   Added trigger and pulse pins for ping sensor
'''

class RoverPins():
    BUZZER_PIN = 24
    #BUTTON_BUZZER_PIN = 24
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
    PING_TRIGGER_PIN = 0
    PING_PULSE_PIN = 0
    
