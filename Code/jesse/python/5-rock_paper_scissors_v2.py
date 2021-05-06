'''
After playing, ask them if they'd like to play again. If they say yes, restart the game, otherwise exit.
'''

import random

# list of all three options
options = ['rock', 'paper', 'scissors']

# list of winning messages
tie = '\nTie game!'
lose = '\nSorry, you lose!'
win = '\nCongratulations, you win!'

while True:
    # get computer's choice at random
    computer = random.choice(options)

    # get user's choice, continue ony if valid entry
    while True:
        player = input('\nEnter "rock", "paper", or "scissors": ').lower()
        if player in options:
            break
        else:
            print('\nInvalid entry.')

    # determine who won and inform the user
    if player == 'rock':
        if computer == 'rock':
            print(tie)
        elif computer == 'paper':
            print(lose)
        elif computer == 'scissors':
            print(win)
    if player == 'paper':
        if computer == 'rock':
            print(win)
        elif computer == 'paper':
            print(tie)
        elif computer == 'scissors':
            print(lose)
    if player == 'scissors':
        if computer == 'rock':
            print(lose) 
        if computer == 'paper':
            print(win)
        if computer == 'scissors':
            print(tie)
            
    # loop again after asking user if they would like to continue playing
    # valid entry required
    while True:
        again = input('\nWould you like to play again? Enter "yes" or "no": ').lower()
        if again == 'yes':
            break
        elif again == 'no':
            exit()
        else:
            print('\nInvalid entry')