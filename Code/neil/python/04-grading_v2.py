'''
Grading

Part 2

Find the specific letter grade (A+, B-, etc). You can check for more 
specific ranges using if statements, or use modulus % to get the ones-digit 
to set another string to '+', '-', or ' '. Then you can concatenate that string 
with your grade string.

'''

# Part 2

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
