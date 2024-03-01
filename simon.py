import time
import random
import os


def game():
    first_pick = 1
    last_pick = 3

    os.system('cls')
    
    def simon_says(first_pick, last_pick):
        sequence = ''
        print('Memorize the following sequence: \n')
        time.sleep(3)
        os.system('cls')
        while first_pick <= last_pick:
            pick = random.choice('0123456789')
            print(pick)
            time.sleep(1)
            os.system('cls')
            sequence += pick
            first_pick += 1
            time.sleep(1)

        os.system('cls')

        player = input('Enter the sequence: ')

        if player == sequence:
            print('Good job\n')
            time.sleep(2)
            os.system('cls')
            first_pick = 1
            last_pick += 1
            simon_says(first_pick, last_pick)
        else:
            print('Game over')
            first_pick = 1
            last_pick = 3
    
    simon_says(first_pick, last_pick)
game()