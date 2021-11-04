'''
Aces can be worth 11 if they won't put the total point value of both cards over 21. Remember that you can have multiple aces in a hand. Try generating a list of all possible hand values by doubling the number of values in the output whenever you encounter an ace. For one half, add 1, for the other, add 11. This ensures if you have multiple aces that you account for the full range of possible values.
'''

# get, test and append each card entry
def verify_card(card):
    face_cards = ['K', 'Q', 'J', 'A']
    card = card.upper()
    if card.isdigit() and 2 <= int(card) <= 10:
        return card  
    elif card in face_cards:
        return card
    else:
        return verify_card(input('Invalid entry. Enter a valid number or face card: '))

# get cards from user
card1 = verify_card(input('What\'s your first card? '))
card2 = verify_card(input('What\'s your second card? '))
card3 = verify_card(input('What\'s your third card? '))

cards = [card1, card2, card3]

print(cards)

# tally score of cards
score = []
for card in cards:
    if card.isdigit() == False:
        if card == 'A':
            if 21 - sum(score) < 11:
                score.append(1)
            else:
                score.append(11)
        else:
            score.append(10)
    else:
        score.append(int(card))
print(score)

score = sum(score)
# give player advice based on score of three cards
message = ''
if score < 17:
    message = 'Hit!'
elif 17 <= score < 21:
    message = 'Stay!'
elif score == 21:
    message = 'Blackjack!'
elif score > 21:
    message = 'Already busted!'

print(f'score: {score}. {message}')