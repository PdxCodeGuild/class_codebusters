'''def go_hiking(energy, weather):
    if energy == "spry":
        if weather == "sunny":
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
    num = abs(num)
    if 9 < num < 100:
        return True


def test_double_digit():
    assert double_digit(5) == False
    assert double_digit(55) == True
    assert double_digit(672) == False
    assert double_digit(-56) == True


# Opposite
# Write a function that takes two integers, `a` and `b`, and returns `True` if one is positive and the other is negative, and return `False` otherwise.

def opposite(a, b):
    if a < 0 > b or b < 0 > a:
        return True
    return False


def test_opposite():
    assert opposite(10, -1) == True
    assert opposite(2, 3) == False
    assert opposite(-1, -1) == False


# Near 100
# Write a function that returns True if a number within 10 of 100.


def near_100(num):
    if 94 < + num <= 106:
        return True
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
    if b > a and b > c:
        return b
    if c > a and c > b:
        return b


def test_maximum_of_three():
    assert maximum_of_three(5, 6, 2) == 6
    assert maximum_of_three(-4, 3, 10) == 10'''


def double_letters(word):
    word = input('anyword: ')
    print(word)
    wordlist = list.word
    print(wordlist*2)
