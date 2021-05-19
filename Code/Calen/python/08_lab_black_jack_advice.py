# Blackjack Advice
# Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. +
# First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

# Less than 17, advise to "Hit"
# Greater than or equal to 17, but less than 21, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"
# Print out the current total point value and the advice.

# What's your first card? Q
# What's your second card? 2
# What's your third card? 3
# 15 Hit

# What's your first card? K
# What's your second card? 5
# What's your third card? 5
# 20 Stay

# What's your first card? Q
# What's your second card? J
# What's your third card? A
# 21 Blackjack!
# Version 2 (optional)
# Aces can be worth 11 if they won't put the total point value of both cards over 21. Remember that you can have multiple aces in a hand. Try generating a list of all possible hand values by doubling the number of values in the output whenever you encounter an ace. For one half, add 1, for the other, add 11. This ensures if you have multiple aces that you account for the full range of possible values.


# First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
while True:
    cards = []
    aces_count = 0
    acceptable_cards = ['a','k','q','j', 10, 9, 8, 7, 6, 5, 4, 3, 2, 1,]
    for i in range(3):
        x = input(f'Please input card number {i+1}:  ').lower()
        try:
            x = int(x)
        except ValueError:
            pass # this will keep us from getting errors when converting letters to int type. 
        cards.append(x)

    # lets make a quality control system to verify input
    bad_input = False
    for card in cards:
        if card not in acceptable_cards:
            bad_input = True
    
    if bad_input == False:
        break
    print(f'Looks like one of the cards you entered was not a valid card, \n Your current cards: {cards} \n Acceptable card inputs: {acceptable_cards} \n Please retry with valid input.')



# Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

for i in range(len(cards)):
    
    if cards[i] == 'a':
        cards[i] = 1
        aces_count += 1

    
    elif cards[i] in ['k','q','j']:
        cards[i] = 10


# Less than 17, advise to "Hit"
# Greater than or equal to 17, but less than 21, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"
# Print out the current total point value and the advice.


hand_sum = sum(cards)
# I am so damn funny.


while aces_count > 0:
    # this is basically saying, for every ace counted during facecard conversion, 
    # see if there is head-room for the optional 10point value of each ace and take advantage of as much as able without busting 21.
    if hand_sum + 10 < 21:
        hand_sum += 10
    
    aces_count -= 1




if hand_sum < 17:
    advice = f'Due to your hand of {hand_sum} being under 17 total points you are reccomended to hit.'

elif hand_sum > 21:
    advice = 'Your hand is over 21 points! You are a-bust.'

elif hand_sum == 21:
    advice = 'You scored a perfect black-jack at 21 points.'

else: # else must be over 17, but less than 21
    advice = f'you are advised to hold being at {hand_sum} total points out of 21.'

print(advice)