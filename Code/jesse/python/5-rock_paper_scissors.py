'''
Let's play rock-paper-scissors with the computer. You may want to try using these emojis 🗿📃✂️✊✋✌

The computer will ask the user for their choice (rock, paper, scissors)
The computer will randomly choose rock, paper or scissors
Determine who won and tell the user
Let's list all the cases:

rock vs rock (tie)
rock vs paper
rock vs scissors
paper vs rock
paper vs paper (tie)
paper vs scissors
scissors vs rock
scissors vs paper
scissors vs scissors (tie)
'''

import random

# list of all three options
options = ['rock', 'paper', 'scissors']

# get computer's choice at random
computer = random.choice(options)

# get user's choice, continue ony if valid entry
while True:
    player = input('\nEnter rock, paper, or scissors: ').lower()
    if player in options:
        break
    else:
        print('\nInvalid entry.')

# list of winning messages
tie = '\nTie game!\n'
lose = '\nSorry, you lose!\n'
win = '\nCongratulations, you win!\n'

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