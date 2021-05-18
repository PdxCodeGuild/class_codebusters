"""
Let's write a python program to give basic blackjack playing advice during a game 
by asking the player for cards. First, ask the user for three playing cards 
(A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of 
each card individually. Number cards are worth their number, all face cards are 
worth 10. At this point, assume aces are worth 1. Use the following rules to 
determine the advice:

Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
Print out the current total point value and the advice.
"""
# imports
import random

# functions
# make a card
def make_card(input):
    if input in tens:
        input = '10'
    if input in aces:
        input = '1'
    input = int(input) 
    return input

# computer advice
def advice(h):
    if h == 21:
        return 'Blackjack'
    elif h > 21:
        return 'Busted'
    elif h >= 17:
        return 'stay'
    elif h < 17:
        return 'hit'

# cards
cards = ['A', 'a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'j', 'Q', 'q',
 'K', 'k',]

tens = ['J', 'j', 'Q', 'q', 'K', 'k']
aces = ['A', 'a'] 
# generate player hand
first_card = input("What's your first card?")
if first_card not in cards:
        first_card = input('Please select a calid card: ')
second_card = input("What's your second card?")
if second_card not in cards:
        second_card = input('Please select a valid card: ')
third_card = input("What's your third card?")
if third_card not in cards:
        third_card = input('Please select a valid card: ')

# convert hand
hand = make_card(first_card) + make_card(second_card) + make_card(third_card)


print(f'{hand} {advice(hand)}')










