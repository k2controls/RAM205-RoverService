import time

def test_sonar_ping(rover):
    
    print("Testing sonar ping.")
    print()
    print("Sonar should display a distance.")
    print("Place obstacle to test.")
    print("Enter to number of 1 second samples to display.")
    count = int(input("sample count = "))
    for i in range(count):
        print(f"d = {rover.sonar.distance}") 
        time.sleep(1)
    return 1

