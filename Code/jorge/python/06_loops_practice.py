# Practice 3: While and For Loops
# Copy and paste this file into your own "03_loops.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 03_loops.py"

# Double Numbers
# Write a function that takes a list of numbers and returns a new list with every number doubled


def double_numbers(nums):
    for i in range(len(nums)):
        nums[i] *= 2
    return nums


def test_double_numbers():
    assert double_numbers([1, 2, 3]) == [2, 4, 6]
