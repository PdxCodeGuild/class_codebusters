'''

Grading

Part 1

Let's convert a number grade to a letter grade, using if and elif statements and comparisons. First have the user enter a number representing the grade (0-100). Then convert the number grade to a letter grade.

Concepts Covered:

fundamentals, comparisons & conditionals
Numeric Ranges:

90-100: A
80-89: B
70-79: C
60-69: D
0-59: F
Part 2

Find the specific letter grade (A+, B-, etc). You can check for more specific ranges using if statements, or use modulus % to get the ones-digit to set another string to '+', '-', or ' '. Then you can concatenate that string with your grade string.

'''

# Part 1

# Prompt user to enter number grade
user_grade = int(input('Please enter number grade: '))
# Go through conditional statements to store the appropriate letter grade
if user_grade < 60:
    grade = 'F'

elif user_grade >= 60 and user_grade < 70:
    grade = 'D'

elif user_grade >= 70 and user_grade < 80:
    grade = 'C'

elif user_grade >= 80 and user_grade < 90:
    grade = 'B'

elif user_grade >= 90:
    grade = 'A'

print(f'The letter grade is: {grade}')  # Display letter grade to user
