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
Version 3: Complete

Future Improvements:

- Fix Version two to not use a nested if statement
- Add better loser message based on outcome

'''

#-----------------------------------------------#
# Import Dependencies
#-----------------------------------------------#
import random
choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
win_rock = ["Lizard", "Scissors"]
win_paper = ["Spock", "Rock"]
win_sci = ["Lizard", "Paper"]
win_liz = ["Spock", "Paper"]
win_spock = ["Scissors", "Rock"]

#-----------------------------------------------#
# Compare Choices
#-----------------------------------------------#

def throw_choice(user_input, comp_input):
    if user_input == comp_input:
        return "It was a Tie"
    elif user_input == "Rock" and comp_input in win_rock:
        return "You win! Rock crushes scissors and lizards"
    elif user_input == "Paper" and comp_input in win_paper:
        return "You win! Paper disproves spock and covers rock"
    elif user_input == "Scissors" and comp_input in win_sci:
        return "You win! Scissors cuts paper and lizards"
    elif user_input == "Lizard" and comp_input in win_liz:
        return "You win! Lizards eat paper and poison Spock"
    elif user_input == "Spock" and comp_input in win_spock:
        return "You win! Spock vaporizes rock and smashes scissors"
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
    -------------------------------------------------------------------------
    You have been chosen.

    Make your selection: Rock, Paper, Scissors, Lizard, Spockor, or Exit: 
    -------------------------------------------------------------------------
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

        # If the user wants to play again, loop back
        if again_choice == "Yes":
            continue
        # If the user does not want to play anymore, break the loop
        else:
            break
    elif user_choice == "Exit":
        break
    # If the user put in invalid data, ask for it again
    else:
        print("Please input a valid selection")
        continue
