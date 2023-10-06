import time
import sys
import random

try:
    while True:  # The main program loop
        print('█' * random.randint(1,20))
        time.sleep(0.1)  # Pause for 1/10 of a second
except KeyboardInterrupt:
    sys.exit()
