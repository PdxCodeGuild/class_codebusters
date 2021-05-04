'''
Grading
Part 1

Let's convert a number grade to a letter grade, using if and elif statements and comparisons.
First have the user enter a number representing the grade (0-100).
Then convert the number grade to a letter grade.
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

    return f'Your grade is {grade}.'


print(grading())
