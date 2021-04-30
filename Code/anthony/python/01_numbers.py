# Practice 1: Numbers & Arithmetic
# Copy and paste this file into your own "01_numbers.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 01_numbers.py"

# Is Even
# Write a function returns whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False


def test_is_even():
    assert is_even(5) == False
    assert is_even(6) == True

# Ones Digit
# Write a function that returns the ones digit of a number


def ones_digit(num):
    if type(num) is not int:
        return -1
    ones_digit = num % 10
    return ones_digit


def test_ones_digit():
    assert ones_digit(3) == 3
    assert ones_digit(56) == 6
    assert ones_digit(812) == 2
    assert ones_digit("hello") == -1


# Percentage
# Write a function that takes two integers, a value and a maximum, and returns a string representing the percentage as an integer

def percentage(v, max):
    if max == 0:
        return None
    percent = v / max * 100
    if percent > 1:
        percent = int(percent)
    return f"{percent}%"


def test_precentage():
    assert percentage(1, 10) == '10%'
    assert percentage(600, 1200) == '50%'
    assert percentage(1, 3) == '33%'
    assert percentage(5, 0) == None
    assert percentage(1000, 10) == '10000%'
    assert percentage(1, 1000) == '0.1%'
