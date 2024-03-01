import time
import random
import os

first_pick = 1

last_pick = 3

sequence = ''

while first_pick <= last_pick:
    pick = random.choice('0123456789')
    print(pick)
    sequence += pick
    first_pick += 1
    time.sleep(1)

os.system('cls')

player = input('Enter the sequence: ')

if player == sequence:
    print('Good job')
else:
    print('Game over')