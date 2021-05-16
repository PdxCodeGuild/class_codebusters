"""
Blackjack Advice

Let's write a python program to give basic blackjack playing advice 
during a game by asking the player for cards. First, ask the user for 
three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
Then, figure out the point value of each card individually. 
Number cards are worth their number, all face cards are worth 10. 
At this point, assume aces are worth 1. Use the following rules to determine the advice:

    Less than 17, advise to "Hit"
    Greater than or equal to 17, but less than 21, advise to "Stay"
    Exactly 21, advise "Blackjack!"
    Over 21, advise "Already Busted"

Print out the current total point value and the advice.
"""
# import random
import random


# create a card dictionary
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

# create list for random choice
card_list = ['A', '2', '3', '4', '5',
             '6', '7', '8', '9', '10', 'J', 'Q', 'K']


# function to get and return 3 cards
def get_three_cards():
    ''' A three legged dog walks into a bar.  He hops on a barstool, looks
        around the place with steely eyes and says, "I'm looking for the
        man who shot my paw!"
    '''
    input('Press the "return"  key to get 3 cards.')
    first_round = []
    c = 3
    while c != 0:
        card = random.choice(card_list)
        if c == 3:
            print(f'Your first card is {card}.')
        elif c == 2:
            print(f'Your second card is {card}.')
        else:
            print(f'Your third card is {card}.')
        first_round.append(card)
        c -= 1
    return first_round


# # RESERVED FOR FUTURE USE (Actually, I used this for dispay before I really
# # saw how you wanted the output and I didn't want to remove it from my code.
# convert the cards to a string to display
# def convert_to_string(the_cards):
#     card_selection = ''
#     for i in the_cards:
#         print(the_cards[i])
#         card_selection += (i + ', ')
#     return card_selection


# add up the cards and display the results
def add_cards(the_cards, cards):
    sum_of_3_cards = 0
    for i in range(len(the_cards)):
        sum_of_3_cards += cards[the_cards[i]]
    if sum_of_3_cards < 17:
        return f'The cards add up to {sum_of_3_cards}.  I advise Hit'
    elif sum_of_3_cards >= 17 and sum_of_3_cards < 21:
        return f'The cards add up to {sum_of_3_cards}.  I advise Stay'
    elif sum_of_3_cards == 21:
        return 'Blackjack!!  You win!'
    else:
        return f'You are over 21 with {sum_of_3_cards}. Busted!'


if __name__ == '__main__':
    # print(cards)  # for testing
    the_cards = (get_three_cards())
    # print(convert_to_string(the_cards))  # for future call
    print(add_cards(the_cards, cards))
