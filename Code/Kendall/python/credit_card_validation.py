numbers = '4556737586899855'

# Convert the input string into a list of ints
credit_card = []
for num in numbers:
    credit_card.append(int(num))

print(credit_card)

# Slice off the last digit. That is the check digit.
last_digit = int(credit_card.pop())
print(last_digit)

# Reverse the digits.
credit_card.reverse()
print(credit_card)

# Double every other element in the reversed list.
for i in range(0, len(credit_card), 2):
    credit_card[i] *= 2

print(credit_card)

# Subtract nine from numbers over nine.
for i in range(0, len(credit_card)):
    if credit_card[i] > 9:
        credit_card[i] -= 9

print(credit_card)

# Sum all values.
total = sum(credit_card)
print(total)

# Take the second digit of that sum.
check_digit = str(total)[1]
print(check_digit)

# If that matches the check digit, the whole card number is valid.
if int(check_digit) == last_digit:
    print('Valid')
else:
    print('Invalid')
