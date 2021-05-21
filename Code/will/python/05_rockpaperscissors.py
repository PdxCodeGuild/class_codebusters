'''
Let's play rock-paper-scissors with the computer. 
You may want to try using these emojis 🗿📃✂️✊✋✌

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

while True:
    choices = ['rock', 'paper', 'scissors']
    user = input('Choose rock, paper or scissors: ')
    print(f'User chose: {user}')
    computer = random.choice(choices)
    print(f'Computer chose: {computer}')

    if user == computer:
        print('Its a tie')
    elif user == 'rock' and computer == 'paper':
        print('Computer wins')
    elif (user == 'rock' and computer == 'scissors'):
        print('User wins')
    elif (user == 'paper' and computer == 'paper'):
        print('Its a tie')
    elif (user == 'paper' and computer == 'rock'):
        print('Computer wins')
    elif (user == 'paper' and computer == 'scissors'):
        print('User wins')
    elif (user == 'scissors' and computer == 'scissors'):
        print('Its a tie')
    elif (user == 'scissors' and computer == 'rock'):
        print('Computer wins')
    elif (user == 'scissors' and computer == 'paper'):
        print('User wins')

    play_again = input('Would you like to play again?  yes or no? ')
    if play_again == 'no':
        break
