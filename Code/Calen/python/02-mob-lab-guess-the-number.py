# coded in mob platform 

"""
Let's play 'Guess the Number'. The computer will guess a random int between 1 and 10. 
The user will then try to guess the number, and the program will tell them whether they're right or wrong.

Part 1
Using a while loop, allow the user to guess 10 times. If they fail to guess the number after 10 tries, the user is told they've lost. 
If the user guesses the number, the user is told they've won and the game exits. You can get a random number using random.randint:

import random
x = random.randint(1,10)
print(x)
Below is an example run of the game:

guess the number: 5
try again!
guess the number: 2
try again!
guess the number: 3
correct! you guessed 3 times
"""


'''
Part 2
Allow the user to make an unlimited number of guesses using a while True and break. Keep track of how many guesses the user has made, and tell them at the end.
'''

'''
Part 3
Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.
'''

'''
Part 4 (optional)
Tell the user whether their current guess is closer than their last. This can be done by maintaining a variable containing the last guess outside the loop, then comparing the last guess to the current guess, and check if it's closer. Hint: you're interested in comparing the two absolute differences: abs(current_guess-target) and abs(last_guess-target).

'''

'''
Part 5 (optional)
Swap the user with the computer: the user will pick a number, and the computer will make random guesses until they get it right.
'''

import random



guess = input("guess a number between 1-10:  ")
guess = int(guess)
y = 0

while True:

    y += 1
    
    x = random.randint(1,10)

    if x == guess:
        print(f'You won, {guess} was the number! You guess {y} times!')
        break

    elif y == 1:
        if x > guess:
            print(f'Sorry, guess again. {x} was not the number. Your guess was too high')
        else:
            print(f'Sorry, guess again. {x} was not the number. Your guess was too low')

    elif abs(last_x - guess) > abs(x - guess):
        print(f"The computer guess of {x} is closer to the number, than The computer last guess of {last_x}")

    elif abs(last_x - guess) < abs(x - guess):
        print(f"The computer guess of {x} is farther from the number, than The computer last guess of {last_x}")

    elif last_x == x:
        print('You guessed the same thing twice.')

    elif abs(last_x - guess) == abs(x - guess):
        print(f"The distance between The computer current guess of {x}, and The computer prior guess of {last_x} is the same.")

    last_x = x
















# x = random.randint(1,10)
# y = 0

# while True:

#     y += 1
#     guess = input("Guess a number between 1-10:  ")
#     guess = int(guess)

#     if guess == x:
#         print(f'You won, {x} was the number! You guess {y} times!')
#         break

#     elif y == 1:
#         if guess > x:
#             print(f'Sorry, guess again. {guess} was not the number. Your guess was too high')
#         else:
#             print(f'Sorry, guess again. {guess} was not the number. Your guess was too low')

#     elif abs(last_guess - x) > abs(guess - x):
#         print(f"Your guess of {guess} is closer to the number, than your last guess of {last_guess}")

#     elif abs(last_guess - x) < abs(guess - x):
#         print(f"Your guess of {guess} is farther from the number, than your last guess of {last_guess}")

#     elif last_guess == guess:
#         print('You guessed the same thing twice.')

#     elif abs(last_guess - x) == abs(guess - x):
#         print(f"The distance between your current guess of {guess}, and your prior guess of {last_guess} is the same.")

#     last_guess = guess







# version 3
# x = random.randint(1,10)
# y = 0

# while True:

#     y += 1
#     guess = input("Guess a number between 1-10:  ")
#     guess = int(guess)

#     if guess == x:
#         print(f'You won, {x} was the number! You guess {y} times!')
#         break

#     else: 
#         if guess > x:
#             print(f'Sorry, guess again. {guess} was not the number. Your guess was too high')
#         else:
#             print(f'Sorry, guess again. {guess} was not the number. Your guess was too low')







# Version two 
"""
y = 0
while True:
    x = random.randint(1,10)
    y += 1
    guess = input("Guess a number between 1-10:  ")
    guess = int(guess)

    if guess == x:
        print(f'You won, {x} was the number! You guess {y} times!')
        break

    else: 
        print(f'Sorry, guess again. {guess} was not the number. {x} was the number, you guessed {y} times.')
    

"""
# verion one
# x = random.randint(1,10)
# y = 0
# while y < 10:
#     guess = input("Guess a number between 1-10:  ")
#     guess = int(guess)

#     if guess == x:
#         print(f'You won, {x} was the number!')
#         break

#     else: 
#         print(f'Sorry, guess again. {guess} was not the number.')
    
#     y += 1

#     if y == 10:
#         print('You have ran out of tries. Thank you for playing.')