from Bluetooth.MessageServiceMock import MessageService


def do_tests():
    print("Test Message Service - a smartphone connect is required!")
    print("Press LED OFF button to exit.")
    ms = MessageService()
    messageService = ""
    while message != "0,0,0,0,0,0,1,0,0": #LED OFF button 
        message = ms.get_message()
        print(message)
    print()
