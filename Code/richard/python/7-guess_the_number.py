# Guess the Number
# Let's play 'Guess the Number'. The computer will guess a random int between 1 and 10. The user will 
# then try to guess the number, and the program will tell them whether they're right or wrong.

# Part 1
# Using a while loop, allow the user to guess 10 times. If they fail to guess the number after 10 tries,
#  the user is told they've lost. If the user guesses the number, the user is told they've won and the 
# game exits. You can get a random number using random.randint:

import random

theNumber = random.randint(0,10)
'''
i = 1

while i < 11:
    guess = int(input("Guess the number: "))
    if guess == theNumber:
        print(f"Correct! You guessed {i} times!")
        break
    else:
        print('Try Again!')
    i += 1
'''

# Part 2
# Allow the user to make an unlimited number of guesses using a while True and break. Keep track of how 
# many guesses the user has made, and tell them at the end.
'''
theNumber = random.randint(0,10)

i = 1

while True:
    guess = int(input("Guess the number: "))
    if guess == theNumber:
        print(f"Correct! You guessed {i} times!")
        break
    else:
        print('Try Again!')
    i += 1
'''
# Part 3
# Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.
'''
theNumber = random.randint(0,10)

i = 1

while True:
    guess = int(input("Guess the number: "))
    if guess == theNumber:
        print(f"Correct! You guessed {i} times!")
        break
    elif guess > theNumber:
        print("Too High!")
    else:
        print('Too Low!')
    i += 1
'''
# Part 4 (optional)
# Tell the user whether their current guess is closer than their last. This can be done by maintaining 
# a variable containing the last guess outside the loop, then comparing the last guess to the current 
# guess, and check if it's closer. Hint: you're interested in comparing the two absolute differences: 
# abs(current_guess-target) and abs(last_guess-target).
'''
theNumber = random.randint(0,10)

i = 1
lastGuess = 0

while True:
    guess = int(input("Guess the number: "))
    if guess == theNumber:
            print(f"Correct! You guessed {i} times!")
            break
    elif i == 1:
        if guess > theNumber:
            print("Too High!")
        else:
            print('Too Low!')
    else:
        if abs(guess - theNumber) < abs(lastGuess - theNumber):
            print("Getting Closer!")
            
        else:
            print('Getting Further!')
    i += 1
    lastGuess = guess
'''
# Part 5 (optional)
# Swap the user with the computer: the user will pick a number, and the computer will make random 
# guesses until they get it right.
'''
theNumber = int(input("Pick a number from 0 to 10: "))

i = 1
lastGuess = 0

while True:
    guess = random.randint(0,10)
    if guess == theNumber:
            print(f"Computer guesses {guess} and it\'s Correct! Computer guessed the number in {i} tries!")
            break
    elif i == 1:
        if guess > theNumber:
            print(f"Computer guesses {guess} and it\'s Too High!")
        else:
            print(f'Computer guesses {guess} and it\'s Too Low!')
    else:
        if abs(guess - theNumber) < abs(lastGuess - theNumber):
            print(f"Computer guesses {guess} and it\'s Getting Closer!")
            
        else:
            print(f'Computer guesses {guess} and it\'s Getting Further!')
    i += 1
    lastGuess = guess
'''