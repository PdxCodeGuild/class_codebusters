'''

Rock Paper Scissors

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
Version 2 (optional)

After playing, ask them if they'd like to play again. If they say yes, restart the game, otherwise exit.

Version 3 (optional)

Rock, paper, scissors, lizard, Spock! https://www.instructables.com/id/How-to-Play-Rock-Paper-Scissors-Lizard-Spock/

'''
# Version 1

import random

# comp asks user for choice
user_choice = input('Pick 1 and enter your answer -- Rock, paper, or scissors?: ').lower()

choices = ['rock', 'paper', 'scissors']
# comp will randomly choose rock, paper, or scissors
comp_choice = random.choice(choices)

# determine who won and tell the user
if user_choice == 'rock' and comp_choice == 'rock':
    print("It's a tie!")

elif user_choice == 'rock' and comp_choice == 'paper':
    print("You lost!")

elif user_choice == 'rock' and comp_choice == 'scissors':
    print("You won!")

if user_choice == 'paper' and comp_choice == 'paper':
    print("It's a tie!")

elif user_choice == 'paper' and comp_choice == 'scissors':
    print("You lost!")

elif user_choice == 'paper' and comp_choice == 'rock':
    print("You won!")

if user_choice == 'scissors' and comp_choice == 'scissors':
    print("It's a tie!")

elif user_choice == 'scissors' and comp_choice == 'rock':
    print("You lost!")

elif user_choice == 'scissors' and comp_choice == 'paper':
    print("You won!")