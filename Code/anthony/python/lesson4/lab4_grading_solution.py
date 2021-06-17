"""
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
"""
import utils

grade = utils.get_int("What was your grade: ")


while True:
    if grade <= 100 and grade >= 0:
        if grade >= 90 and grade <= 105:
            letter_grade = "A"
        elif grade >= 80:
            letter_grade = "B"
        elif grade >= 70:
            letter_grade = "C"
        elif grade >= 60:
            letter_grade = "D"
        else:
            letter_grade = "F"
        break
    else:
        grade = int(input("Invalid number. Enter an integer between 0 - 100"))

print(letter_grade)
