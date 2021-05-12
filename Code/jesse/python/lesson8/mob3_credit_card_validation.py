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

# Convert the input string into a list of ints
number = '4556737586899855'
credit_card = []
for num in number:
    credit_card.append(int(num))

# Slice off the last digit. That is the check digit.
last_digit = credit_card.pop()

# Reverse the digits.
credit_card.reverse()

# Double every other element in the reversed list.
doubled = []
for i in range(len(credit_card)):
    if i % 2 == 0:
        multiplied = credit_card[i] * 2
        doubled.append(multiplied)
    else:
        doubled.append(credit_card[i])

# Subtract nine from numbers over nine.
for i in range(len(doubled)):
    if doubled[i] > 9:
        doubled[i] -= 9     

# Sum all values.
sum_total = 0
for num in doubled:
    sum_total += num

# Take the second digit of that sum.
second_digit = sum_total % 10

# If that matches the check digit, the whole card number is valid.
if second_digit == last_digit:
    print('Valid.')
else:
    print('Not valid.')