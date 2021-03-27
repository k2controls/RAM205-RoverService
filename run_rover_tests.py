from Rover.Rover import Rover
from tests import rover_tests

def do_tests():
    try:
        input("Press enter to start Rover testing.")
        print()
        rover = Rover()
        rover_tests(rover)
        print("Test complete.")
    except Exception as ex:
        print(ex)
        rover = None

if __name__ == "__main__":
    do_tests()