
"""
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
"""
from random import choice

# create a function to play rock paper scissors
r = '\U0001F5FF'
p = '\U0001F4C3'
s = '\U00002702 \U0000FE0F'
#print("\U00002702 \U0000FE0F")


def rps():
    # get and validate the input from the user
    while True:
        choice_rps = input(
            f'Enter your choice of rock{r}, paper{p}, or scissors{s}: ').lower()

        if choice_rps == 'rock' or choice_rps == 'paper' or choice_rps == 'scissors':
            break
        else:
            print('You must make a valid selection')

    return choice_rps


# play the game
def play_rps():
    rps_list = ['rock', 'paper', 'scissors']
    computer_rps = choice(rps_list)

    user_choice = rps()
    if user_choice == computer_rps:
        print('You tied!')
    elif user_choice == 'paper' and computer_rps == 'rock':
        print('You won, paper covers rock!')
    elif user_choice == 'paper' and computer_rps == 'scissors':
        print('You lost, scissors cuts paper!')
    elif user_choice == 'rock' and computer_rps == 'paper':
        print('You lost, paper covers rock!')
    elif user_choice == 'rock' and computer_rps == 'scissors':
        print('You won, rock crushes scissors!')
    elif user_choice == 'scissors' and computer_rps == 'rock':
        print('You lost, rock crushes scissors!')
    else:
        print('You win, scissors cuts paper!')


if __name__ == '__main__':
    play_rps()
