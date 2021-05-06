#-----------------------------------------------#
'''
PDX Code Guild
Class CodeBusters
Week 02
Lab 05 - Rock Paper Scissors
Jared Nistler
'''
#-----------------------------------------------#
# Instructions
#-----------------------------------------------#
'''
VERSION 1
Let's play rock-paper-scissors with the computer. 
You may want to try using these emojis 🗿📃✂️✊✋✌

The computer will ask the user for their choice (rock, paper, scissors)
The computer will randomly choose rock, paper or scissors
Determine who won and tell the user

rock vs paper

rock vs scissors
paper vs rock
paper vs scissors
scissors vs rock
scissors vs paper

VERSION 2
After playing, ask them if they'd like to play again. 
If they say yes, restart the game, otherwise exit.

VERSION 3
Rock, paper, scissors, lizard, Spock!

'''
#-----------------------------------------------#
# Developer Notes
#-----------------------------------------------#
'''
Version 1: Complete
Version 2: Complete
Version 3: Under Development

Future Improvements:

- Fix Version two to not use a nested if statement

'''

#-----------------------------------------------#
# Import Dependencies
#-----------------------------------------------#
import random
choices = ["Rock", "Paper", "Scissors"]

#-----------------------------------------------#
# Compare Choices
#-----------------------------------------------#

def throw_choice(user_input, comp_input):
    if user_input == comp_input:
        return "It was a Tie"
    elif (user_input == "Paper" and comp_input == "Rock") or (user_input == "Scissors" and comp_input == "Paper") or (user_input == "Rock" and comp_input == "Scissors"):
        return "You win!!"
    else:
        return "You lose. Womp womp."

def end_message (user, comp, result):
    return f'''
    ------------------------------------------------
    You threw {user}, the computer threw {comp}
    {result}
    ------------------------------------------------

    '''

#-----------------------------------------------#
# User Input and Start Game
#-----------------------------------------------#

while True: 
    # Prompt user for input
    user_choice = input (f'''
    ------------------------------------------------
    You have been chosen.

    Make your selection: Rock, Paper, Scissors, or Exit: 
    ------------------------------------------------
    ''').title()

    # Validate input and start game
    if user_choice in choices:
        # Computer selects random choice
        comp_choice = random.choice(choices)
        # Compare the results
        result = throw_choice(user_choice, comp_choice)
        # Print the result message
        print(end_message(user_choice, comp_choice, result))
        
        # Ask the player if they want to play again
        again_choice = input(f'''
        
        Would you like to play again? Yes or No.
        ''').title()

        if again_choice == "Yes":
            continue
        else:
            break
    elif user_choice == "Exit":
        break
    else:
        continue
