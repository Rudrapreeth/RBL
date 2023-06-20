import random
import time

class OCM:

    def __init__(self, threshold_value1, threshold_value2):
        self.threshold_value1 = threshold_value1
        self.threshold_value2 = threshold_value2
        self.current_value = 0
        self.alarm = False

    def measure_current(self):
        self.current_value = random.randint(0, 1000)

    def detect_attack(self):
        if self.current_value > self.threshold_value1:
            self.alarm = True
        elif self.current_value > self.threshold_value2:
            self.alarm = True

    def reset(self):
        self.alarm = False

def main():
    ocm = OCM(100, 200)

    # Get user input for threshold values
    threshold_value1 = str(input("Enter threshold value 1: "))
    threshold_value2 = str(input("Enter threshold value 2: "))

    # Detect side-channel attack
    for i in range(10):
        ocm.measure_current()
        ocm.detect_attack()

    if ocm.alarm:
        print("Side-channel attack detected!")
    else:
        print("No side-channel attack detected.")

    # Detect fault injection attack
    for i in range(10):
        ocm.measure_current()
        ocm.detect_attack()

    if ocm.alarm:
        print("Fault injection attack detected!")
    else:
        print("No fault injection attack detected.")

    # Detect invasive attack
    for i in range(10):
        ocm.measure_current()
        ocm.detect_attack()

    if ocm.alarm:
        print("Invasive attack detected!")
    else:
        print("No invasive attack detected.")

if __name__ == "__main__":
    main()
