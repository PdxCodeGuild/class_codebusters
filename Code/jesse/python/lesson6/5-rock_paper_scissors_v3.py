'''
Rock, paper, scissors, lizard, Spock! https://www.instructables.com/id/How-to-Play-Rock-Paper-Scissors-Lizard-Spock/
'''
'''
rock vs rock (tie)
rock vs paper (lose)
rock vs scissors (win)
rock vs lizard (win)
rock vs spock (lose)
paper vs rock (win)
paper vs paper (tie)
paper vs scissors (lose)
paper vs lizard (lose)
paper vs spock (win)
scissors vs rock (lose)
scissors vs paper (win)
scissors vs scissors (tie)
scissors vs lizard (win)
scissors vs spock (lose)
lizard vs rock (lose)
lizard vs paper (win)
lizard vs scissors (lose)
lizard vs lizard (tie)
lizard vs spock (win)
spock vs rock (win)
spock vs paper (lose)
spock vs scissors (win)
spock vs lizard (lose)
spock vs spock (tie)
'''

import random

# list of all five options
options = ['rock', 'paper', 'scissors', 'lizard', 'spock']

# list of winning messages
tie = '\nTie game!'
lose = '\nSorry, you lose!'
win = '\nCongratulations, you win!'

while True:
    # get computer's choice at random
    computer = random.choice(options)

    # get user's choice, continue ony if valid entry
    while True:
        player = input('\nEnter "rock", "paper", "scissors", "lizard", or "spock": ').lower()
        if player in options:
            break
        else:
            print('\nInvalid entry.')

    # show computer's choice
    print(f'\nThe computer chose {computer}')

    # determine who won and inform the user
    if player == 'rock':
        if computer == 'rock':
            print(tie)
        elif computer == 'paper':
            print(lose)
        elif computer == 'scissors':
            print(win)
        elif computer == 'lizard':
            print(win)
        elif computer == 'spock':
            print(lose)
    if player == 'paper':
        if computer == 'rock':
            print(win)
        elif computer == 'paper':
            print(tie)
        elif computer == 'scissors':
            print(lose)
        elif computer == 'lizard':
            print(lose)
        elif computer == 'spock':
            print(win)
    if player == 'scissors':
        if computer == 'rock':
            print(lose) 
        elif computer == 'paper':
            print(win)
        elif computer == 'scissors':
            print(tie)
        elif computer == 'lizard':
            print(win)
        elif computer == 'spock':
            print(lose)
    if player == 'lizard':
        if computer == 'rock':
            print(lose)
        elif computer == 'paper':
            print(win)
        elif computer == 'scissors':
            print(lose)
        elif computer == 'lizard':
            print(tie)
        elif computer == 'spock':
            print(win)
    if player == 'spock':
        if computer == 'rock':
            print(win)
        elif computer == 'paper':
            print(lose)
        elif computer == 'scissors':
            print(win)
        elif computer == 'lizard':
            print(lose)
        elif computer == 'spock':
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

