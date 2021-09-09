#-----------------------------------------------#
'''
PDX Code Guild
Class CodeBusters
Week 04
Lab 08 - Blackjack Advice
Jared Nistler
'''
#-----------------------------------------------#
# Instructions
#-----------------------------------------------#
'''
Let's write a python program to give basic blackjack 
playing advice during a game by asking the player for 
cards. First, ask the user for three playing cards 
(A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, 
figure out the point value of each card individually. 
Number cards are worth their number, all face cards 
are worth 10. At this point, assume aces are worth 1. 
Use the following rules to determine the advice:

-Less than 17, advise to "Hit"
-Greater than or equal to 17, but less than 21, advise to "Stay"
-Exactly 21, advise "Blackjack!"
-Over 21, advise "Already Busted"

'''
#-----------------------------------------------#
# Developer Notes
#-----------------------------------------------#
'''
Version 1: Complete
Version 2: Complete

Future Improvements:

- Sorting method may have some unforseen inefficiencies

'''

#-----------------------------------------------#
# Import Dependencies
#-----------------------------------------------#


#-----------------------------------------------#
# Define Globals
#-----------------------------------------------#
# Defines a dictionary with card values
card_values = {
    'A': [1, 11],
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}

#-----------------------------------------------#
# Define Functions
#-----------------------------------------------#

def advice_analysis(value):
    '''
    Defines a function that takes in a blackjack score as
    an int and returns a string message providing the user
    with adivce
    '''
    if value < 17:
        message = "Hit"
    elif value >= 17 and value < 21:
        message = "Stay"
    elif value == 21:
        message = "Blackjack!"
    else:
        message = "You are Already Busted"
    return message

def sort_cards (cards):
    '''
    Defines a function that takes in a list of cards and 
    returns the list sorted with any Aces at the end
    '''
    sorted_cards = []
    for card in cards:
        # If the card is an Ace, add to the end of the list
        if card == 'A':
            sorted_cards.append(card)
        else:
            # If the card is not an Ace, add to the beginning of list
            sorted_cards.insert(0, card)
    return sorted_cards


def sum_cards(cards):
    '''
    Defines a function that takes in a list of cards and 
    returns a list of possible values for the hand
    '''
    total = 0
    for i in range(len(cards)):
        # If the card isn't an Ace, add the value to the total
        if cards[i] != 'A':
            total += card_values[cards[i]]
        # If the first card is an Ace, all cards are Aces
        elif i == 0:
            return [3, 13, 23, 33]
        # If the second card is an Ace, add to total with all possibilities
        elif i == 1:
            return [total + 2, total + 12, total + 22]
        # If the third card is an Ace, add to total with all possibilities
        elif i == 2:
            return [total + 1, total + 11]
    # If there are no Aces, return the summed total
    return [total]

#-----------------------------------------------#
# User Input
#-----------------------------------------------#

# Prompt user for input and validate
while True:
    card1 = input("What's your first card? ").upper()
    if card1 in card_values:
        break
    else:
        continue

while True:
    card2 = input("What's your second card? ").upper()
    if card2 in card_values:
        break
    else:
        continue
while True:
    card3 = input("What's your third card? ").upper()
    if card3 in card_values:
        break
    else:
        continue

# Create card list
card_list = [card1, card2, card3]
# Sort cards to have Aces at the back of the hand
card_list = sort_cards(card_list)

#-----------------------------------------------#
# Print Advice
#-----------------------------------------------#

# Creates a list of possible scores with hand
poss_scores = sum_cards(card_list)

if len(poss_scores) == 1:
    print(f'''------------------------------
You are at {poss_scores[0]}
{advice_analysis(poss_scores[0])}
------------------------------''')

else:
    for i in range (len(poss_scores)):
        print(f'''------------------------------
{i+1}. You could have {poss_scores[i]}
If You Want this Hand, {advice_analysis(poss_scores[i])}
------------------------------''')