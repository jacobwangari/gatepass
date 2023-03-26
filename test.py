from pyfirmata import Arduino, util
import time

board = Arduino('com3')

board.digital[13].write(1)

    