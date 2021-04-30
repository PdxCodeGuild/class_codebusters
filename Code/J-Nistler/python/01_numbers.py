#-----------------------------------------------#
# PDX Code Guild
# Class CodeBusters
# Week 01
# Practice 01 - Numbers
# Jared Nistler
#-----------------------------------------------#

# Is Even
# Write a function returns whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

def is_even(a):
    if a%2 == 0:
        return True
    else:
        return False

def test_is_even():
    assert is_even(5) == False
    assert is_even(6) == True

# Ones Digit
# Write a function that returns the ones digit of a number

def ones_digit(num):
    str_num = str(num)
    str_lst_dig = (str_num[-1])
    return int(str_lst_dig)

def test_ones_digit():
    assert ones_digit(3) == 3
    assert ones_digit(56) == 6
    assert ones_digit(812) == 2


# Percentage
# Write a function that takes two integers, a value and a maximum, and returns a string representing the percentage as an integer

def percentage(v, max):
    num_dec = v/max
    num_per = num_dec * 100
    int_per = int(num_per)
    return str(int_per) + "%"

def test_precentage():
    assert percentage(1, 10) == '10%'
    assert percentage(600, 1200) == '50%'
    assert percentage(1, 3) == '33%'