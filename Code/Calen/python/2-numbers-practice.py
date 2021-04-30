## Code copied from:
# https://github.com/PdxCodeGuild/class_codebusters/blob/main/1%20Python/03%20Numbers%20%26%20Arithmetic/numbers_practice.py
## Edited by calen ray


# Practice 1: Numbers & Arithmetic
# Copy and paste this file into your own "01_numbers.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 01_numbers.py"

# Is Even
# Write a function returns whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

import math

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
    solution = str(num)
    solution = solution[-1]
    solution = int(solution)
    return solution

def test_ones_digit():
    assert ones_digit(3) == 3
    assert ones_digit(56) == 6
    assert ones_digit(812) == 2


# Percentage
# Write a function that takes two integers, a value and a maximum, and returns a string representing the percentage as an integer


# I am not going to lie, I could probably do this with fewer lines but its functional and I am happy with it. 
def percentage(v, max):
    solution = v/max
    solution = int(solution*100)
    solution = str(solution)
    solution += '%'
    return solution

def test_precentage():
    assert percentage(1, 10) == '10%'
    assert percentage(600, 1200) == '50%'
    assert percentage(1, 3) == '33%'

