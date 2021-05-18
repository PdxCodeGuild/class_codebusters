"""
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
import random


def rps_game():
    valid_choices = ['r', 'p', 's']
    # The computer will ask the user for their choice(rock, paper, scissors)
    win = "You won!"
    lose = "You lost"

    while True:
        user = 'x'
        while user[0] not in valid_choices:
            user = input("Choose rock, paper, or scissors (r,p,s): ").lower()

        # The computer will randomly choose rock, paper or scissors
        computer = random.choice(valid_choices)

        # Determine who won and tell the user

        if user[0] == computer:
            print("It was a draw")
        elif user[0] == "r":
            if computer == "s":
                print(win)
            else:
                print(lose)
        elif user[0] == "s":
            if computer == "p":
                print(win)
            else:
                print(lose)
        else:
            if computer == "r":
                print(win)
            else:
                print(lose)

        play_again = input("Do you want to play again (Y/n)? ").lower()
        if play_again in ['yes', 'y', 'yeah', 'sure', 'ok', '']:
            continue
        else:
            break

    print("Thanks for playing")


if __name__ == "__main__":
    rps_game()
