import time
import pyfirmata


board = pyfirmata.Arduino('com3')  


red_pin = 6
green_pin = 5
blue_pin = 4

board.digital[red_pin].mode = pyfirmata.OUTPUT
board.digital[green_pin].mode = pyfirmata.OUTPUT
board.digital[blue_pin].mode = pyfirmata.OUTPUT

while True:
    # Set the LED to red
    board.digital[red_pin].write(1)
    board.digital[green_pin].write(0)
    board.digital[blue_pin].write(0)
    time.sleep(2)

    # Set the LED to blue
    board.digital[red_pin].write(0)
    board.digital[green_pin].write(0)
    board.digital[blue_pin].write(1)
    time.sleep(3)

    # Set the LED to green
    board.digital[red_pin].write(0)
    board.digital[green_pin].write(1)
    board.digital[blue_pin].write(0)
    time.sleep(1)

    