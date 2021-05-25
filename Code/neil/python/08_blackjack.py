'''

Blackjack Advice

Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
Print out the current total point value and the advice.

What's your first card? Q
What's your second card? 2
What's your third card? 3
15 Hit

What's your first card? K
What's your second card? 5
What's your third card? 5
20 Stay

What's your first card? Q
What's your second card? J
What's your third card? A
21 Blackjack!
Version 2 (optional)

Aces can be worth 11 if they won't put the total point value of both cards over 21. Remember that you can have multiple aces in a hand. Try generating a list of all possible hand values by doubling the number of values in the output whenever you encounter an ace. For one half, add 1, for the other, add 11. This ensures if you have multiple aces that you account for the full range of possible values.

'''

# Version 1

# Create dictionary of cards
cards = {
    'A': 1,
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
input("Welcome to Blackjack Advice! Please\n only choose from the following choices:\n (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)\n --Press 'Enter' to continue...-- ")
# Ask user for first card
first_card = input("What's your first card?: ").upper()
# Ask user for second card
second_card = input("What's your second card?: ").upper()
# Ask user for third card
third_card = input("What's your third card?: ").upper()

# Loop through cards dictionary to provide values to user input
for card in cards:

    value = cards[card]

    if first_card == card:
        first_card = value

    if second_card == card:
        second_card = value

    if third_card == card:
        third_card = value

total = first_card + second_card + third_card

# Display total and provide advice via conditional statements
if total < 17:
    print(f'{total} Hit')

elif total >= 17 and total < 21:
    print(f'{total} Stay')

elif total == 21:
    print(f'{total} Blackjack!')

elif total > 21:
    print(f'{total} Already Busted')
