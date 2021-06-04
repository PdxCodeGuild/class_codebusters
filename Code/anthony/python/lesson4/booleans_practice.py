
# Practice 2: Booleans, Comparisons, & Conditionals
# Copy and paste this file into your own "02_booleans.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 02_booleans.py"


# Go Hiking
# Write a function that takes a string indicating energy level and weather


def go_hiking(energy, weather):
    # return energy == 'spry' and weather == 'sunny'

    # nice_weather = ['sunny', 'partly cloudy']
    # moods = ['spry', 'energetic']

    # if energy in moods and weather in nice_weather:
    #     return True
    # else:
    #     return False

    if energy == 'spry':
        if weather == 'sunny':
            return True
    return False


def test_go_hiking():
    assert go_hiking('tired', 'rainy') == False
    assert go_hiking('tired', 'sunny') == False
    assert go_hiking('spry', 'rainy') == False
    assert go_hiking('spry', 'sunny') == True


# Double Digit
# Write a function that returns True if the number is a double digit

def double_digit(num):
    # return 9 < abs(num) < 100

    # number = abs(num)
    # number = str(number)
    # return len(number) == 2

    num = abs(num)
    if num > 9 and num < 100:
        return True
    return False


def test_double_digit():
    assert double_digit(5) == False
    assert double_digit(55) == True
    assert double_digit(672) == False
    assert double_digit(-56) == True


# Opposite
# Write a function that takes two integers, `a` and `b`, and returns `True` if one is positive and the other is negative, and return `False` otherwise.

def opposite(a, b):
    # return (a > 0 and b < 0) or (a < 0 and b > 0)

    if a < 0 or b < 0:
        if a > 0 or b > 0:
            return True
        else:
            return False
    else:
        return False

    # if a < 0 or b < 0:
    #     if a > 0 or b > 0:
    #         return True
    # return False


def test_opposite():
    assert opposite(10, -1) == True
    assert opposite(2, 3) == False
    assert opposite(-1, -1) == False


# Near 100
# Write a function that returns True if a number within 10 of 100.


def near_100(num):
    # return num in range(90, 110)
    # return True if 90 <= num <= 110 else False

    difference = 100 - num
    return difference <= 10 and difference >= -10


def test_near_100():
    assert near_100(50) == False
    assert near_100(99) == True
    assert near_100(105) == True
    assert near_100(115) == False


# Maximum of Three
# Write a function that returns the maximum of 3 parameters.


def maximum_of_three(a, b, c):
    # return max(a, b, c)

    # if a > b and a > c:
    #     return a
    # elif b > a and b > c:
    #     return b
    # else:
    #     return c

    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max


def test_maximum_of_three():
    assert maximum_of_three(5, 6, 2) == 6
    assert maximum_of_three(-4, 3, 10) == 10
