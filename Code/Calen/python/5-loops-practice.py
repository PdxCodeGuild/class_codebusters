# copied from https://github.com/PdxCodeGuild/class_codebusters/blob/main/1%20Python/06%20Loops/loops_practice.py
#edited by Calen Ray    

# Practice 3: While and For Loops
# Copy and paste this file into your own "03_loops.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 03_loops.py"

# Double Numbers
# Write a function that takes a list of numbers and returns a new list with every number doubled


def double_numbers(nums):
    new_nums = []
    for x in nums:
        new_nums.append(x*2)   
    return new_nums

def test_double_numbers():
    assert double_numbers([1, 2, 3]) == [2, 4, 6]


# Stars
# Write a function that takes an integer and returns that number of asterisks in a string

def stars(n):
    return n*'*'

def test_stars():
    assert stars(1) == '*'
    assert stars(2) == '**'
    assert stars(3) == '***'
    assert stars(4) == '****'


# Extract Less Than Ten
# Write a function to move all the elements of a list with value less than 10 to a new list and return it.

# I mean I'll do it, but I dont know why we wouldnt just .pop the list for anything over 10. 

def extract_less_than_ten(nums):
    new_list = []
    for x in nums:
        if x <= 10:
            new_list.append(x)
    return new_list

def test_extract_less_than_ten():
    assert extract_less_than_ten([2, 8, 12, 18]) == [2, 8]

