from enum import Enum

class Commands(Enum):
    STOP                = 0
    FORWARD             = 1
    BACKWARD            = 2
    LEFT                = 4
    RIGHT               = 5
    LEFT_ALT            = 6
    RIGHT_ALT           = 7
    BEEP                = 8
    SPEED_UP            = 9
    SPEED_DOWN          = 10
    SERVO_LEFT          = 11
    SERVO_RIGHT         = 12
    LED_OFF             = 13
    LED_RED             = 14
    LED_GREEN           = 15
    LED_BLUE            = 16
    SERVO_MID           = 17
    OUTFIRE             = 18
    
    GIMBAL_UP           = 20
    GIMBAL_DOWN         = 21
    GIMBAL_RIGHT        = 22
    GIMBAL_LEFT         = 23
    GIMBAL_BTN_RELEASE  = 24
    #ANALOG MESSAGES
    SERVO_ANALOG        = 100     #REQUIRES VALUE 
    LED_RED_ANALOG      = 101     #REQUIRES VALUE 
    LED_GREEN_ANALOG    = 102     #REQUIRES VALUE 
    LED_BLUE_ANALOG     = 103     #REQUIRES VALUE 
    #MODE MESSAGES
    COLORFUL_STOP       = 200
    COLORFUL_START      = 201
    TRACTING_STOP       = 202
    TRACTING_START      = 203
    OBSTACLE_START      = 204
    OBSTACLE_STOP       = 205
