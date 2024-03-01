import time
import random
import os


def game():
    first_pick = 1
    last_pick = 3
    
    def simon_says(first_pick, last_pick):
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
            print('Good job\n')
            first_pick = 1
            last_pick += 1
            simon_says(first_pick, last_pick)
        else:
            print('Game over')
            first_pick = 1
            last_pick = 3
    
    simon_says(first_pick, last_pick)
game()