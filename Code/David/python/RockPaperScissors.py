import random
a = True
while a:
    user = input("Choose rock, paper, or scissors: ")

    computer = ["rock", "paper", "scissors"]  # choices for random
    'rock' > "scissors" > 'paper' > 'rock'  # establish game rules
    choice = random.choice(computer)  # get computers choice
    print('I chose ' + choice)  # lets user know what computer chose

    if user > choice:  # let user know who won
        print('Crap, You win')  # sore loser
    if choice > user:
        print('Haha, I win')  # jerk
    if choice == user:
        print('Great minds think alike.')  # ties happen
    next = input('would you like to play again, yes or no? ')

    if next == 'no':
        a = False  # ends game
        print('Id be scared to play me too, goodbye')  # still a jerk
