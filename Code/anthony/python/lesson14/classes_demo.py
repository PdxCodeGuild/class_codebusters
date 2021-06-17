
import random
import math

# Lists


def distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx*dx + dy*dy)


# p1 = [5, 2]
# p2 = [8, 4]
# print(distance(p1, p2))


# Dictionaries
def distance(p1, p2):
    dx = p1['x'] - p2['x']
    dy = p1['y'] - p2['y']
    return math.sqrt(dx*dx + dy*dy)


# p1 = {'x': 5, 'y': 2}
# p2 = {'x': 8, 'y': 4}
# print(distance(p1, p2))

# class Point:
#     def __init__(self, x, y):  # this is the initializer
#         self.x = x  # these are member variables
#         self.y = y

#     def distance(self, p):  # method, or 'member function'
#         dx = self.x - p.x
#         dy = self.y - p.y
#         return math.sqrt(dx*dx + dy*dy)

#     def __repr__(self):
#         return f"{self.x}, {self.y}"


# p1 = Point(5, 2)  # call the initializer, instantiate the class
# p2 = Point(8, 4)
# print(p1.y)
# print(p2.y)
# print(type("hello"))
# print(type(p1))
# print(p1.distance(p2))
# print(str(p1))


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def get_value(self):
        if self.value in ['J', 'Q', 'K']:
            return 10
        elif self.value == "A":
            return 1
        else:
            return self.value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

    def __gt__(self, other):
        if self.get_value() > other.get_value():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.get_value() >= other.get_value():
            return True
        else:
            return False


deck = []
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

for suit in suits:
    for value in values:
        deck.append(Card(suit, value))

random.shuffle(deck)
hand = [deck.pop(), deck.pop()]
print(hand)
while True:
    hit_or_stay = input("Hit or stay? ").lower()
    if hit_or_stay == 'hit':
        hand.append(deck.pop())
    else:
        print(hand)
