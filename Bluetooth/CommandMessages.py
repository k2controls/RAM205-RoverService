from Bluetooth.Commands import Commands

class CommandMessages():

    MODE_MESSAGES = {
        "4WD,MODE20":   Commands.TRACTING_STOP,
        "4WD,MODE21":   Commands.TRACTING_START,
        "4WD,MODE30":   Commands.OBSTACLE_STOP,
        "4WD,MODE31":   Commands.OBSTACLE_START,
        "4WD,MODE40":	Commands.COLORFUL_STOP,
        "4WD,MODE41":	Commands.COLORFUL_START
        }

    ANALOG_MESSAGES = {
        "PTZ":  Commands.SERVO_ANALOG,
        "CLR":  Commands.LED_RED_ANALOG,
        "CLG":  Commands.LED_GREEN_ANALOG,
        "CLB":  Commands.LED_BLUE_ANALOG
    }
        
    BUTTON_MESSAGES = {
        "0,0,0,0,0,0,0,0,0": Commands.STOP
        ,"1,0,0,0,0,0,0,0,0": Commands.FORWARD
        ,"2,0,0,0,0,0,0,0,0": Commands.BACKWARD
        ,"3,0,0,0,0,0,0,0,0": Commands.LEFT
        ,"4,0,0,0,0,0,0,0,0": Commands.RIGHT
        ,"0,1,0,0,0,0,0,0,0": Commands.LEFT_ALT
        ,"0,2,0,0,0,0,0,0,0": Commands.RIGHT_ALT
        ,"0,0,1,0,0,0,0,0,0": Commands.BEEP
        ,"0,0,0,1,0,0,0,0,0": Commands.SPEED_UP
        ,"0,0,0,2,0,0,0,0,0": Commands.SPEED_DOWN
        ,"0,0,0,0,1,0,0,0,0": Commands.SERVO_LEFT
        ,"0,0,0,0,2,0,0,0,0": Commands.SERVO_RIGHT
        ,"0,0,0,0,0,0,1,0,0": Commands.LED_OFF
        ,"0,0,0,0,0,0,2,0,0": Commands.LED_RED
        ,"0,0,0,0,0,0,3,0,0": Commands.LED_GREEN
        ,"0,0,0,0,0,0,4,0,0": Commands.LED_BLUE
        ,"0,0,0,0,0,0,0,0,1": Commands.SERVO_MID
        ,"0,0,0,0,0,0,0,1,0": Commands.OUTFIRE
        ,"0,0,0,0,0,0,8,0,0": Commands.LED_OFF
        ,"0,0,0,0,3,0,0,0,0": Commands.GIMBAL_UP
        ,"0,0,0,0,4,0,0,0,0": Commands.GIMBAL_DOWN
        ,"0,0,0,0,7,0,0,0,0": Commands.GIMBAL_RIGHT
        ,"0,0,0,0,6,0,0,0,0": Commands.GIMBAL_LEFT 
        ,"0,0,0,0,8,0,0,0,0": Commands.GIMBAL_BTN_RELEASE
    }

