import os
import time

GPIO_LED = "17"
GPIO_BUTTON = "27"
GPIO_SYSFS = "/sys/class/gpio/"
GPIO_LED_PATH = os.path.join(GPIO_SYSFS, "gpio"+GPIO_LED)
GPIO_BUTTON_PATH = os.path.join(GPIO_SYSFS, "gpio"+GPIO_BUTTON)

def write_GPIO(filename, value):
    with open(filename, "w") as file:
        file.write(value)

def read_GPIO(filename):
    with open(filename) as file:
        content = file.read()
        return content

def main():
    print("\nStarting the toggleLED program\n")
    print("----------------------------\n")
    time.sleep(1)

    print("Setting up the LED on the GPIO\n")
    write_GPIO(GPIO_SYSFS+"export", GPIO_LED)
    time.sleep(0.1)
    write_GPIO(GPIO_LED_PATH+"/direction", "out")

    time.sleep(1)

    print("Setting up the BUTTON on the GPIO\n\n")
    write_GPIO(GPIO_SYSFS+"export", GPIO_BUTTON)
    time.sleep(0.1)
    write_GPIO(GPIO_BUTTON_PATH+"/direction", "in")
    time.sleep(1)

    print("-- Toggle LED with push button or close the program: ctrl+c --")
    
    while True:
        content = read_GPIO(GPIO_BUTTON_PATH+"/value")

        if "1" in content:
            write_GPIO(GPIO_LED_PATH+"/value", "1")
        else:
            write_GPIO(GPIO_LED_PATH+"/value", "0")

        time.sleep(0.1)

try:
    main()
except KeyboardInterrupt:
    time.sleep(1)
    print("\n\nClosing the LED on the GPIO\n")
    write_GPIO(GPIO_SYSFS+"unexport", GPIO_LED)
    time.sleep(0.5)
    print("Closing the BUTTON on the GPIO\n")
    write_GPIO(GPIO_SYSFS+"unexport", GPIO_BUTTON)
    time.sleep(1)
    print("\n----------------------------")
    print("Finished the toggleLED Program\n\n")
except:
    print("\n\nOther error occured!")
    time.sleep(1)
    print("Closing the LED on the GPIO\n")
    write_GPIO(GPIO_SYSFS+"unexport", GPIO_LED)
    time.sleep(0.5)
    print("Closing the BUTTON on the GPIO\n")
    write_GPIO(GPIO_SYSFS+"unexport", GPIO_BUTTON)
    time.sleep(1)
    print("\n----------------------------")
    print("Finished the toggleLED Program\n\n")