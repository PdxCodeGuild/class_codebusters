# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.


def validate_card(card_number):
    # Return false if not 16 digits
    if len(card_number) != 16:
        return False
    try:
        int_card = [int(num) for num in card_number]
    except ValueError:
        return False
    check_digit = int_card.pop()
    reversed_card = reversed(int_card)
    doubled_digits = [num if i %
                      2 else num*2 for i, num in enumerate(reversed_card)]
    reduced_card = [num - 9 if num > 9 else num for num in doubled_digits]
    total = sum(reduced_card)
    return True if total % 10 == check_digit else False


card = '4556737586899855'
print(validate_card(card))
