import time
import random

first_pick = 1

last_pick = 3

while first_pick <= last_pick:
    print(random.choice('0123456789'))
    first_pick += 1
    time.sleep(1)