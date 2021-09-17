# Created a list for user inputs and face cards
cards = []
face_cards = ['J', 'K', 'Q']


card_1 = input('What\'s your first card? ')
cards.append(card_1)
card_2 = input('What\'s your second card? ')
cards.append(card_2)
card_3 = input('What\'s your third card? ')
cards.append(card_3)

for num in cards:
    if num in face_cards:
        cards[cards.index(num)] = 10
    elif num == 'A':
        cards[cards.index(num)] = 1
    else:
        cards[cards.index(num)] = int(num)

score = sum(cards)
if score < 17:
    print(f'{score} Hit')
elif 17 <= score < 21:
    print(f'{score} Stay')
elif score == 21:
    print(f'{score} Blackjack')
elif score > 21:
    print(f'{score} Already Busted')
