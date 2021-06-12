'''
Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. 
First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. 
At this point, assume aces are worth 1. Use the following rules to determine the advice:

Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"

Print out the current total point value and the advice.
'''

# assign values to each card. numbers are equal to numbers. face value cards are 10. Aces are 10
cards = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
         '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

# input statement asking the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K).
first_card = input("What is your first card?  ")
second_card = input("What is your second card? ")
third_card = input("What is your third card? ")

first_value = cards[first_card]
second_value = cards[second_card]
third_value = cards[third_card]
sum_of_cards = first_value + second_value + third_value


# if statement for advice
if sum_of_cards < 17:
    print(f"{sum_of_cards} Hit")
elif sum_of_cards >= 17 and sum_of_cards < 21:
    print(f"{sum_of_cards} Stay")
elif sum_of_cards == 21:
    print(f"{sum_of_cards} Blackjack!")
elif sum_of_cards < 21:
    print(f"{sum_of_cards} Busted")
