"""
Author: Calen Ray
Date: 4/28/21
project: Turtle
hint: Goto the bottom for special projects.
"""

from turtle import *
import random 



right(55)

forward(100)

back(100)

right (65)

forward(100)

back(100)

left(210)

forward(175)

left(150)

forward(50)

back(50)

right(300)

forward(50)

back(50)

left(150)

forward(50)

left(90)

forward(25)

right(90)

forward(50)

right(90)

forward(50)

right(90)

forward(50)

right(90)

forward(25)


done()


"""

#--------------------------------------------------------------------#

# this is used to take user input and run a random forward, left, and right function the specified amount of times. 
user_input = input(f'Please provide a random number')
user_input = float(user_input)


i = 0

while i < user_input:
    rand_number = random.randint(1, 100)
    forward(rand_number)
    if rand_number > 150:
        rand_number = random.randint(1, 250)
        right(rand_number)
    else:
        rand_number = random.randint(1, 250)
        left(rand_number)
    i += 1
done()

"""
"""
#--------------------------------------------------------------------#

# this will allow the user to direct the turtle:

ok_directions = ['right', 'left', 'forward', 'straight', 'back', 'finished'] # this will allow us to keep users from inputing garbage 

while True: # allows us to break the game and halt.

    while True:

        direction = input("What direction would you like to go?")
        direction = direction.lower()

        if direction in ok_directions:
            break
        else:
            print(f'That was not a recognized direction please choose from the following list: \n {ok_directions}')
    
    while True:

        if direction == 'finished':
            break

        length = input('And how far would you like to go? \n use numbers between -250 through 250')
        try:
            length = float(length)
        except:
            pass
        if length > 250 or length < -250:
            print("Your distance is out of range")
        else:
            break
    
    # if forward
    if direction == 'forward' or direction == 'straight':
        forward(length)
    
    #if back
    elif direction == 'back':
        back(length)
    
    elif direction == 'right':
        right(length)
    
    elif direction == 'left':
        left(length)
    
    else:
        print("Thank you for playing my game.")
    

"""

