from Rover.rover_factory import make_rover
from tests.test_rover import test_rover

def do_tests():
    try:
        input("Press enter to start Rover testing.")
        print()
        rover = make_rover()
        test_rover(rover)
        print("Test complete.")
    except Exception as ex:
        print(ex)
        rover = None

if __name__ == "__main__":
    do_tests()
