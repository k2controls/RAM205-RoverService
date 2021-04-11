''' Runs bluetooth tests
'''
import time

from Bluetooth.MessageServiceMock import MessageService
from Bluetooth.CommandService import CommandService
from Rover.rover_factory import make_rover
from RoverService import RoverService
from Controllers.ControlPadController import ControlPadController
from Rover.Buzzer import BuzzerStatus
from Rover.RoverDrive import DriveMotion
from Rover.RGBLed import LED_COLOR
from Rover.LED import LEDStatus

message_service = None
rover_service = None
rover = None
controller = None

def make_rover_service():
    global message_service, rover_service, rover, controller
    
    message_service = MessageService()
    command_queue = list()
    cs = CommandService(message_service ,command_queue)
    rover = make_rover()
    rover_service = RoverService(cs,rover)
    controller = rover_service.controller

def test_buzzer(control_message, status: BuzzerStatus):
    if type(controller) != ControlPadController:
        print("Error - Controller not set to Control Pad")
        return False
    message_service.set_message(control_message)
    time.sleep(1)
    if rover.buzzer.status == status:
        print(f"Control pad buzzer test passed. Command={controller.last_command}")
        return True
    else:
        print(f"Control pad buzzer test failed. Command={controller.last_command}")
        return False

def test_drive(control_message, drive_motion : DriveMotion, speed):
    if type(controller) != ControlPadController:
        print("Error - Controller not set to Control Pad")
        return False
    message_service.set_message(control_message)
    time.sleep(1)
    if rover.rover_drive.drive_motion == drive_motion and rover.rover_drive.speed == speed:
        print(f"Control pad drive test passed. Command={controller.last_command}")
        return True
    else:
        print(f"Control pad drive test failed. Command={controller.last_command}")
        return False

def test_servo(control_message, position):
    if type(controller) != ControlPadController:
        print("Error - Controller not set to Control Pad")
        return False
    message_service.set_message(control_message)
    time.sleep(1)
    if rover.servo.position == position:
        print(f"Control pad servo test passed. Command={controller.last_command}")
        return True
    else:
        print(f"Control pad buzzer test failed. Command={controller.last_command}")
        return False

def test_rgb_led(control_message, led_color: LED_COLOR):
    if type(rover_service.controller) != ControlPadController:
        print("Error - Controller not set to Control Pad")
        return False
    message_service.set_message(control_message)
    time.sleep(1)
    if rover.rgb_led.get_color_value() == led_color.value:
        print(f"Control pad RGB LED test passed. Command={controller.last_command}")
        return True
    else:
        print(f"Control pad RDB LED test failed. Command={controller.last_command}")
        return False

def test_rgb_led_analog(control_message, values):
    if type(rover_service.controller) != ControlPadController:
        print("Error - Controller not set to Control Pad")
        return False
    message_service.set_message(control_message)
    time.sleep(1)
    if rover.rgb_led.red_led.analog_value != values[0]:
        print(f"Control pad RDB LED analog test failed. Command={controller.last_command}")
        print(f"Red led value is {rover.rgb_led.red_led.analog_value}")
        return False
    elif rover.rgb_led.green_led.analog_value != values[1]:
        print(f"Control pad RDB LED analog test failed. Command={controller.last_command}")
        print(f"Green led value is {rover.rgb_led.green_led.analog_value}")
        return False
    elif rover.rgb_led.blue_led.analog_value != values[2]:
        print(f"Control pad RDB LED analog test failed. Command={controller.last_command}")
        print(f"Blue led value is {rover.rgb_led.blue_led.analog_value}")
        return False
    else:
        print(f"Control pad RGB LED test passed. Command={controller.last_command}")
    return True
    
        

def test_control_pad_buzzer():
    print()
    print("Testing buzzer...")
    print("Controller must be configured to toggle buzzer")
    
    message = "0,0,1,0,0,0,0,0,0"  
    status = BuzzerStatus.ON
    if not test_buzzer(message, status):
        print(f"Failed! (message:{message}, status:{status})")
        return False
    
    message = "0,0,1,0,0,0,0,0,0"  
    status = BuzzerStatus.OFF
    if not test_buzzer(message, status):
        print(f"Failed! (message:{message}, status:{status})")
        return False
    return True

def test_control_pad_drive():
    print()
    print("Testing rover drive control...")

    message = "1,0,0,0,0,0,0,0,0"
    motion = DriveMotion.FORWARD
    speed = rover.rover_drive.DEFAULT_SPEED
    if not test_drive(message, motion, speed):
        print(f"Failed! (message:{message}, motion:{motion}, speed:{speed})")
        return False
    
    message = "0,0,0,0,0,0,0,0,0"
    motion = DriveMotion.STOP
    speed = rover.rover_drive.DEFAULT_SPEED
    if not test_drive(message, motion, speed):
        print(f"Failed! (message:{message}, motion:{motion}, speed:{speed})")
        return False
        
    message = "2,0,0,0,0,0,0,0,0"
    motion = DriveMotion.BACKWARD
    speed = rover.rover_drive.DEFAULT_SPEED
    if not test_drive(message, motion, speed):
        print(f"Failed! (message:{message}, motion:{motion}, speed:{speed})")
        return False
    
    message = "3,0,0,0,0,0,0,0,0" 
    motion = DriveMotion.LEFTFORWARD
    speed = rover.rover_drive.DEFAULT_SPEED
    if not test_drive(message, motion, speed):
        print(f"Failed! (message:{message}, motion:{motion}, speed:{speed})")
        return False
    
    message = "4,0,0,0,0,0,0,0,0" 
    motion = DriveMotion.RIGHTFORWARD
    speed = rover.rover_drive.DEFAULT_SPEED
    if not test_drive(message, motion, speed):
        print(f"Failed! (message:{message}, motion:{motion}, speed:{speed})")
        return False
    
    message = "0,1,0,0,0,0,0,0,0" 
    motion = DriveMotion.LEFTROTATE
    speed = rover.rover_drive.DEFAULT_SPEED
    if not test_drive(message, motion, speed):
        print(f"Failed! (message:{message}, motion:{motion}, speed:{speed})")
        return False
    
    message = "0,2,0,0,0,0,0,0,0" 
    motion = DriveMotion.RIGHTROTATE
    speed = rover.rover_drive.DEFAULT_SPEED
    if not test_drive(message, motion, speed):
        print(f"Failed! (message:{message}, motion:{motion}, speed:{speed})")
        return False
    
    message = "0,0,0,1,0,0,0,0,0" 
    motion = DriveMotion.RIGHTROTATE
    speed = rover.rover_drive.DEFAULT_SPEED + rover_service.rover.rover_drive.DELTA_SPEED
    if not test_drive(message, motion, speed):
        print(f"Failed! (message:{message}, motion:{motion}, speed:{speed})")
        return False
    
    message = "0,0,0,2,0,0,0,0,0" 
    motion = DriveMotion.RIGHTROTATE
    speed = rover.rover_drive.DEFAULT_SPEED
    if not test_drive(message, motion, speed):
        print(f"Failed! (message:{message}, motion:{motion}, speed:{speed})")
        return False
    
    return True

def test_control_pad_servo():
    print()
    print("Testing front servo...")
    
    message = "0,0,0,0,1,0,0,0,0"           #SERVO_LEFT
    position = 0
    if not test_servo(message, position):
        print(f"Failed! (message:{message}, position:{position})")
        return False
    
    message = "0,0,0,0,2,0,0,0,0"           #SERVO_RIGHT
    position = 180
    if not test_servo(message, position):
        print(f"Failed! (message:{message}, position:{position})")
        return False
    
    message = "0,0,0,0,0,0,0,0,1"           #SERVO_MID
    position = 90
    if not test_servo(message, position):
        print(f"Failed! (message:{message}, position:{position})")
        return False
    
    message = "4WD,PTZ180"                  #Servo with value of 180 rotation
    position = 180
    if not test_servo(message, position):
        print(f"Failed! (message:{message}, position:{position})")
        return False
    
    message = "4WD,PTZ90"                   #Servo with value of 90 rotation
    position = 90
    if not test_servo(message, position):
        print(f"Failed! (message:{message}, position:{position})")
        return False
    
    message = "4WD,PTZ0"                    #Servo with value of 0 rotation
    position = 0
    if not test_servo(message, position):
        print(f"Failed! (message:{message}, position:{position})")
        return False
    
    return True

def test_control_pad_rgb_led():
    print()
    print("Testing RGB LED...")

    message = "0,0,0,0,0,0,1,0,0"           #LED_OFF
    led_color = LED_COLOR.OFF
    if not test_rgb_led(message, led_color):
        print(f"Failed! (message:{message}, color:{led_color})")
        return False    
    
    message = "0,0,0,0,0,0,2,0,0"           #LED_RED
    led_color = LED_COLOR.RED
    if not test_rgb_led(message, led_color):
        print(f"Failed! (message:{message}, color:{led_color})")
        return False    
    
    message = "0,0,0,0,0,0,3,0,0"           #LED_GREEN
    led_color = LED_COLOR.GREEN
    if not test_rgb_led(message, led_color):
        print(f"Failed! (message:{message}, color:{led_color})")
        return False    
    
    message = "0,0,0,0,0,0,4,0,0"           #LED_BLUE
    led_color = LED_COLOR.BLUE
    if not test_rgb_led(message, led_color):
        print(f"Failed! (message:{message}, color:{led_color})")
        return False    
    
    message = "0,0,0,0,0,0,1,0,0"           #LED_OFF
    led_color = LED_COLOR.OFF
    if not test_rgb_led(message, led_color):
        print(f"Failed! (message:{message}, color:{led_color})")
        return False
    
    return True

def test_control_pad_rgb_led_analog():
    print()
    print("Testing RGB LED analog...")
    
    message = "4WD,CLR255,CLG0,CLB0"    #LED with RGB from 0 to 255 for each
    values = (255, 0, 0)
    if not test_rgb_led_analog(message, values):
        print(f"Failed! (message:{message}, value:{values})")
        return False    
    
    message = "4WD,CLR255,CLG255,CLB255"    #LED with RGB from 0 to 255 for each
    values = (255, 255, 255)
    if not test_rgb_led_analog(message, values):
        print(f"Failed! (message:{message}, value:{values})")
        return False
    
    message = "4WD,CLR100,CLG150,CLB200"    #LED with RGB from 0 to 255 for each
    values = (100, 150, 200)
    if not test_rgb_led_analog(message, values):
        print(f"Failed! (message:{message}, value:{values})")
        return False
    
    message = "4WD,CLR0,CLG0,CLB0"    #LED with RGB from 0 to 255 for each
    values = (0, 0, 0)
    if not test_rgb_led_analog(message, values):
        print(f"Failed! (message:{message}, value:{values})")
        return False
            
    return True
      
def do_tests():
    make_rover_service()
    if not test_control_pad_buzzer():
        print("Failed!")
    elif not test_control_pad_drive():
        print("Failed!")
    elif not test_control_pad_servo():
        print("Failed!")
    elif not test_control_pad_rgb_led():
        print("Failed!")
    elif not test_control_pad_rgb_led_analog():
        print("Failed!")
    else:
        print("Rover Control Pad controller tests passed.")
    print()




