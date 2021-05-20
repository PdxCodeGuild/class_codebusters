'''
Grading
Part 1

Let's convert a number grade to a letter grade, using if and elif statements and comparisons.
First have the user enter a number representing the grade (0-100).
Then convert the number grade to a letter grade.

Part 2

Find the specific letter grade (A+, B-, etc). You can check for more specific ranges using
if statements, or use modulus % to get the ones-digit to set another string to '+', '-',
or ' '. Then you can concatenate that string with your grade string.
'''


# get score and calculate grade
def grading():
    while True:
        score = input('Enter your score: ')
        try:
            score = int(score)
            break
        except ValueError:
            print('Enter a valid score')

    # determine base grade
    if score <= 100 and score >= 90:
        grade = 'A'
    elif score <= 89 and score >= 80:
        grade = 'B'
    elif score <= 79 and score >= 70:
        grade = 'C'
    elif score <= 69 and score >= 60:
        grade = 'D'
    else:
        grade = 'F'

    # determine plus or minus
    range = score % 10
    if grade == 'F':
        plus_minus = ''
    elif score == 100:
        plus_minus = '+'
    elif range <= 3:
        plus_minus = '-'
    elif range >= 7:
        plus_minus = '+'
    else:
        plus_minus = ''

    return f'Your grade is {grade}{plus_minus}.'


print(grading())
