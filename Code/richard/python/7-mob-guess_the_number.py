# Guess the Number
# Let's play 'Guess the Number'. The computer will guess a random int between 1 and 10. 
# The user will then try to guess the number, and the program will tell them whether they're
#  right or wrong.

# Part 1
# Using a while loop, allow the user to guess 10 times. If they fail to guess the number after
#  10 tries, the user is told they've lost. If the user guesses the number, the user is told
#  they've won and the game exits. You can get a random number using random.randint:

import random
#user input
# compGuess = random.randint(1,10)

#print output
# i = 0
# while i < 10:
#     userGuess = int(input("Guess a number: ")) 
#     i += 1
#     if userGuess == compGuess:
#         print(f"Congrats you guessed in {i} tries.")
#         break
#     else:
#         print(f"Try Again, you have {10 - i} tries left.")

# Part 2
# Allow the user to make an unlimited number of guesses using a while True and break. Keep track of how many guesses the 
# user has made, and tell them at the end.

# i = 0
# while True:
#     userGuess = int(input("Guess a number: ")) 
#     i += 1
#     if userGuess == compGuess:
#         print(f"Congrats you guessed in {i} tries.")
#         break
#     else:
#         print(f"Try Again, you've guessed {i} times.")

# Part 3
# Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.

# i = 0
# while True:
#     userGuess = int(input("Guess a number: ")) 
#     i += 1
#     if userGuess == compGuess:
#         print(f"Congrats you guessed in {i} tries.")
#         break
#     elif userGuess < compGuess:
#         print(f"Too Low, you've guessed {i} times.")
    
#     else:
#         print(f"Too High, you've guessed {i} times.")

# Part 4 (optional)
# Tell the user whether their current guess is closer than their last. This can be done by maintaining a variable containing
# the last guess outside the loop, then comparing the last guess to the current guess, and check if it's closer. Hint: you're 
# interested in comparing the two absolute differences: abs(current_guess-target) and abs(last_guess-target).

# i = 0
# lastGuess = 0
# while True:
#     userGuess = int(input("Guess a number: ")) 
#     i += 1
#     if userGuess == compGuess:
#         print(f"Congrats you guessed in {i} tries.")
#         break
#     elif lastGuess > 0:
#         if abs(userGuess - compGuess) > abs(lastGuess - compGuess):
#             print(f"Colder, you've guessed {i} times.")
#         else:
#             print(f"Warmer, you've guessed {i} times.")
#     else:
#         print(f"Try Again, you've guessed {i} times.")
#     lastGuess = userGuess

# Part 5 (optional)
# Swap the user with the computer: the user will pick a number, and the computer will make random guesses until 
# they get it right.

i = 0
userGuess = int(input("Select a number from 1 - 100: "))
guessList = []
while True:
    compGuess = random.randint(1,100)
    i += 1
    while compGuess in guessList:
        compGuess = random.randint(1,100)
    guessList.append(compGuess)
    if userGuess == compGuess:
        print(f"Computer guessed {compGuess} in {i} tries.")
        break
    else:
        print(f"Computer was wrong, it guessed {compGuess}. It has guessed {i} times.")
