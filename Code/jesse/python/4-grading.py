'''
Let's convert a number grade to a letter grade, using if and elif statements and comparisons. First have the user enter a number representing the grade (0-100). Then convert the number grade to a letter grade.

Concepts Covered:

fundamentals, comparisons & conditionals
Numeric Ranges:

90-100: A
80-89: B
70-79: C
60-69: D
0-59: F
'''
# Get score from user and convert to int
score = int(input('Enter a score between 0 and 100: '))

# Convert score into correct grade
# loop until a number between 0 and 100 is entered for score.
while True:
    if score <= 100 and score >= 0:
        if score <= 100 and score >= 90:
            grade = 'A'
        elif score <= 89 and score >= 80:
            grade = 'B'
        elif score <= 79 and score >= 70:
            grade = 'C'
        elif score <= 69 and score >= 60:
            grade = 'D'
        elif score <= 59:
            grade = 'F'
        break

    # ask for a new number if number entered was incorrect
    else:
        score = int(input('Invalid number. Please enter a number between 0 and 100: '))

print(f'A score of {score} is equal to a grade of {grade}')