
"""
Rock Paper Scissors Lizard Spock

Let's play rock-paper-scissors-lizard-spock with the computer.

    The computer will ask the user for their choice (rock, paper, scissors, lizard, or spock)
    The computer will randomly choose rock, paper, scissors, lizard, or spock
    Determine who won and tell the user

Let's list all the cases:
    rock vs rock (tie)
    rock vs paper
    rock vs scissors
    rock vs lizard
    rock vs spock
    paper vs rock
    paper vs paper (tie)
    paper vs scissors
    paper vs lizard
    paper vs spock
    scissors vs rock
    scissors vs paper
    scissors vs scissors (tie)
    scissors vs lizard
    scissors vs spock
    lizard vs rock
    lizard vs paper
    lizard vs scissors
    lizard vs lizard (tie)
    lizard vs spock
    spock vs rock
    spock vs paper
    spock vs scissors
    spock vs lizard
    spock vs spock (tie)

    PHEW!!  Yeah, that's a lot!  This description is as long as the code.
"""
import random


# create a function to get and validate user innput
def rps():
    while True:
        choice_rps = input(
            f'Enter your choice of rock, paper, scissors, lizard, or Spock: ').lower()

        if choice_rps == 'rock' or choice_rps == 'paper' or choice_rps == 'scissors'\
                or choice_rps == 'lizard' or choice_rps == 'spock':
            break
        else:
            print('You must make a valid selection')

    return choice_rps


# play the game
def play_rps():
    # get the computer selection randomly
    rps_list = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    computer_rps = random.choice(rps_list)

    # run rps() function to get usere input
    choice = rps()

    w = 'You won!!'
    l = 'You lost!!'

    if choice == computer_rps:
        return 'You tied!'

    elif choice == 'rock' and computer_rps == 'scissors' or computer_rps == 'lizard':
        return f'{w} Rock crushes scissors' if computer_rps == 'scissors' else f'{w} Rock crushes lizard'

    elif choice == 'rock' and computer_rps == 'paper' or computer_rps == 'spock':
        return f'{l} Paper covers rock' if computer_rps == 'paper' else f'{l} Spock vaporizes rock'

    elif choice == 'paper' and computer_rps == 'rock' or computer_rps == 'spock':
        return f'{w} Paper covers rock!' if computer_rps == 'rock' else f'{w} Paper disproves Spock'

    elif choice == 'paper' and computer_rps == 'scissors' or computer_rps == 'lizard':
        return f'{l} Scissors cuts paper' if computer_rps == 'scissors' else f'{l} Lizard eats paper'

    elif choice == 'scissors' and computer_rps == 'paper' or computer_rps == 'lizard':
        return f'{w} Scissors cuts paper'if computer_rps == 'paper'else f'{w} Scissors decapitates lizard'

    elif choice == 'scissors' and computer_rps == 'rock' or computer_rps == 'spock':
        return f'{l} Rock crushes scissors' if computer_rps == 'rock' else f'{l} Spock smashes scissors'

    elif choice == 'lizard' and computer_rps == 'paper' or computer_rps == 'spock':
        return f'{w} Lizard eats paper' if computer_rps == 'paper'else f'{w} Lizard poisons Spock'

    elif choice == 'lizard' and computer_rps == 'rock' or computer_rps == 'scissors':
        return f'{l} Rock crushes lizard' if computer_rps == 'rock' else f'{l} Scissors decapitates lizard'

    elif choice == 'spock' and computer_rps == 'rock' or computer_rps == 'scissors':
        return f'{w} Spock vaporizes rock' if computer_rps == 'rock' else f'{w} Spock smashes scissors'

    else:
        return f'{l} Paper disproves Spock' if computer_rps == 'paper' else f'{l} Big Lizard poisons Spock'


if __name__ == '__main__':
    print(play_rps())
