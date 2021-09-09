"""
Blackjack Advice
Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
Print out the current total point value and the advice.
"""


def verify_card(card):
    face_cards = ['K', 'Q', 'J', 'A']
    card = card.upper()
    if card.isdigit() and 2 <= int(card) <= 10:
        return card
    elif card in face_cards:
        return card
    else:
        return verify_card(input("Invalid entry. Enter a valid number or face card: "))


def count_cards(cards):
    total = []
    for card in cards:
        if card.isdigit() == False:
            if card == "A":
                if 21 - sum(total) < 11:
                    total.append(1)
                else:
                    total.append(11)
            else:
                total.append(10)
        else:
            total.append(int(card))
    return sum(total)


def advice_analysis(value):
    # Over 21, advise "Already Busted"
    if value > 21:
        message = f"{value} Already busted :("
    # Exactly 21, advise "Blackjack!"
    elif value == 21:
        message = f"{value} Blackjack!"
    # Greater than or equal to 17, but less than 21, advise to "Stay"
    elif value >= 17:
        message = f"{value} Stay"
    # Less than 17, advise to "Hit"
    else:
        message = f"{value} Hit!"

    return message


def main():
    card1 = verify_card(input("What is your first card? "))
    card2 = verify_card(input("What is your second card? "))
    card3 = verify_card(input("What is your third card? "))

    total = count_cards([card1, card2, card3])
    print(advice_analysis(total))


main()
