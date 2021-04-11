from Bluetooth.Commands import Command_ID

class CommandMessages():

    MODE_MESSAGES = {
        "4WD,MODE20":   Command_ID.TRACTING_STOP,
        "4WD,MODE21":   Command_ID.TRACTING_START,
        "4WD,MODE30":   Command_ID.OBSTACLE_STOP,
        "4WD,MODE31":   Command_ID.OBSTACLE_START,
        "4WD,MODE40":	Command_ID.COLORFUL_STOP,
        "4WD,MODE41":	Command_ID.COLORFUL_START
        }

    ANALOG_MESSAGES = {
        "PTZ":  Command_ID.SERVO_ANALOG,
        "CLR":  Command_ID.LED_RED_ANALOG,
        "CLG":  Command_ID.LED_GREEN_ANALOG,
        "CLB":  Command_ID.LED_BLUE_ANALOG
    }
        
    BUTTON_MESSAGES = {
        "0,0,0,0,0,0,0,0,0": Command_ID.STOP
        ,"1,0,0,0,0,0,0,0,0": Command_ID.FORWARD
        ,"2,0,0,0,0,0,0,0,0": Command_ID.BACKWARD
        ,"3,0,0,0,0,0,0,0,0": Command_ID.LEFT
        ,"4,0,0,0,0,0,0,0,0": Command_ID.RIGHT
        ,"0,1,0,0,0,0,0,0,0": Command_ID.LEFT_ALT
        ,"0,2,0,0,0,0,0,0,0": Command_ID.RIGHT_ALT
        ,"0,0,1,0,0,0,0,0,0": Command_ID.BEEP
        ,"0,0,0,1,0,0,0,0,0": Command_ID.SPEED_UP
        ,"0,0,0,2,0,0,0,0,0": Command_ID.SPEED_DOWN
        ,"0,0,0,0,1,0,0,0,0": Command_ID.SERVO_LEFT
        ,"0,0,0,0,2,0,0,0,0": Command_ID.SERVO_RIGHT
        ,"0,0,0,0,0,0,1,0,0": Command_ID.LED_OFF
        ,"0,0,0,0,0,0,2,0,0": Command_ID.LED_RED
        ,"0,0,0,0,0,0,3,0,0": Command_ID.LED_GREEN
        ,"0,0,0,0,0,0,4,0,0": Command_ID.LED_BLUE
        ,"0,0,0,0,0,0,0,0,1": Command_ID.SERVO_MID
        ,"0,0,0,0,0,0,0,1,0": Command_ID.OUTFIRE
        ,"0,0,0,0,0,0,8,0,0": Command_ID.LED_OFF
        ,"0,0,0,0,3,0,0,0,0": Command_ID.GIMBAL_UP
        ,"0,0,0,0,4,0,0,0,0": Command_ID.GIMBAL_DOWN
        ,"0,0,0,0,7,0,0,0,0": Command_ID.GIMBAL_RIGHT
        ,"0,0,0,0,6,0,0,0,0": Command_ID.GIMBAL_LEFT 
        ,"0,0,0,0,8,0,0,0,0": Command_ID.GIMBAL_BTN_RELEASE
    }

