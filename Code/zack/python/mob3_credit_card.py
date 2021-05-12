'''
Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

Convert the input string into a list of ints
Slice off the last digit. That is the check digit.
Reverse the digits.
Double every other element in the reversed list.
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
For example, the worked out steps would be:

4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
85
5
Valid!
'''


def validate_card(user_input): 
    # Verify credit card number length
    if len(user_input) != 16:
        return False

    # Convert the input string into a list of ints
    user_input = list(user_input)

    #list of ints
    try:
        for i in range(len(user_input)):
            user_input[i] = int(user_input[i])

    except ValueError:
        return False   

    # Slice off the last digit. That is the check digit.
    checkdigit = user_input.pop()

    # Reverse the digits.
    user_input.reverse()

    # Double every other element in the reversed list.
    for i in range(0, len(user_input), 2):
        user_input[i] *= 2

    # Subtract nine from numbers over nine.
    for num in range(len(user_input)):
        if user_input[num] > 9:
            user_input[num] -= 9

    # Sum all values.
    user_input = sum(user_input)

    # Take the second digit of that sum.
    while user_input > 99:
        user_input //= 10
    user_input %= 10

    # If that matches the check digit, the whole card number is valid.
    if user_input == checkdigit:
        return True
    return False

# QC:
print(validate_card('4556737586899855'))