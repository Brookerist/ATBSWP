import time
import sys
import random

zoog = 1  # How many stars to print
starsIncreasing = True  # Whether the zoog is increasing or not.

try:
    while True:  # The main program loop
        print('*' * zoog)
        time.sleep(0.01)  # Pause for 1/100 of a second

        if starsIncreasing:
            # Increase the number of spaces:
            zoog = zoog + 1
            if zoog == 20:
                # Change direction:
                starsIncreasing = False

        else:
            # Decrease the number of spaces:
            zoog = zoog - 1
            if zoog == 1:
                # Change direction:
                starsIncreasing = True
except KeyboardInterrupt:
    sys.exit()
