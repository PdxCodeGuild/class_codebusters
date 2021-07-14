# copied from: https://github.com/PdxCodeGuild/class_codebusters/blob/main/1%20Python/04%20Booleans%2C%20Comparisons%2C%20%26%20Conditionals/booleans_practice.py
# edited by: Calen Ray

# Practice 2: Booleans, Comparisons, & Conditionals
# Copy and paste this file into your own "02_booleans.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 02_booleans.py"


# Go Hiking
# Write a function that takes a string indicating energy level and weather


# this could be done more simply but I liked the idea that you could add acceptable terms of travel, you could convert this to a travel indicator of any kind.
def go_hiking(energy, weather):
    good_hiking_weather = ['sunny', 'partly cloudy', 'slight chance of rain', 'clear skies']
    good_hiking_mood = ['spry', 'energetic', 'restlesss', 'bored']
    if energy in good_hiking_mood and weather in good_hiking_weather:
        return True
    else:
        return False

def test_go_hiking():
    assert go_hiking('tired', 'rainy') == False
    assert go_hiking('tired', 'sunny') == False
    assert go_hiking('spry', 'rainy') == False
    assert go_hiking('spry', 'sunny') == True


# Double Digit
# Write a function that returns True if the number is a double digit

def double_digit(num):
    if num < 10 and num > -10:
        return False
    if num > 100 or num < -100:
            return False
    else:
        return True

def test_double_digit():
    assert double_digit(5) == False
    assert double_digit(55) == True
    assert double_digit(672) == False
    assert double_digit(-56) == True


# Opposite
# Write a function that takes two integers, `a` and `b`, and returns `True` if one is positive and the other is negative, and return `False` otherwise.

def opposite(a, b):
    if a > 0 and b < 0:
        return True
    elif a < 0 and b > 0:
        return True
    else:
        return False

def test_opposite():
    assert opposite(10, -1) == True
    assert opposite(2, 3) == False
    assert opposite(-1, -1) == False


# Near 100
# Write a function that returns True if a number within 10 of 100.


def near_100(num):
    if num >= 90 and num <= 110:
        return True
    else:
        return False

def test_near_100():
    assert near_100(50) == False
    assert near_100(99) == True
    assert near_100(105) == True
    assert near_100(115) == False


# Maximum of Three
# Write a function that returns the maximum of 3 parameters.


def maximum_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c


def test_maximum_of_three():
    assert maximum_of_three(5,6,2) == 6
    assert maximum_of_three(-4,3,10) == 10