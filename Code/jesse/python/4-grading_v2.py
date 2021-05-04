'''
Find the specific letter grade (A+, B-, etc). You can check for more specific ranges using if statements, or use modulus % to get the ones-digit to set another string to '+', '-', or ' '. Then you can concatenate that string with your grade string.
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

# add a '+' to the grade if score is 100 or has a second digit of 7-9
# exception: 59 or lower does not get a '+' added
if score == 100 or score % 10 >= 7 and score > 59:
    grade += '+'

# otherwise, add a '-' if the second digit is 0-2
# exception: 59 or less does not get a '-' added[]
elif score % 10 <= 2 and score > 59:
    grade += '-'
    
print(f'A score of {score} is equal to a grade of {grade}')