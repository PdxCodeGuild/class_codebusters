# Grading
# Part 1
# Let's convert a number grade to a letter grade, using if and elif statements and comparisons. First have 
# the user enter a number representing the grade (0-100). Then convert the number grade to a letter grade.
# Concepts Covered:
# fundamentals, comparisons & conditionals
# Numeric Ranges:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# 0-59: F
# Part 2
# Find the specific letter grade (A+, B-, etc). You can check for more specific ranges using if statements, 
# or use modulus % to get the ones-digit to set another string to '+', '-', or ' '. Then you can 
# concatenate that string with your grade string.


def getInt():
    numGrade = int(input("Please enter a number between 0 and 100: "))
    if numGrade > 100 or numGrade < 0:
        numGrade = getInt()
    return numGrade


def getLetterGrade(numberGrade):
    if numberGrade >= 90:
        letGrade = 'A'
    elif numberGrade >= 80:
        letGrade = 'B'
    elif numberGrade >= 70:
        letGrade = 'C'
    elif numberGrade >= 60:
        letGrade = 'D'
    else:
        letGrade = 'F'
    return letGrade

def getPlusMinus(numberGrade):
    modNumberGrade = numberGrade % 10
    if modNumberGrade >= 7 or numberGrade == 100:
        plusMinus = '+'
    elif modNumberGrade >= 4:
        plusMinus = ''
    else:
        plusMinus = '-'
    return plusMinus

intNumGrade = getInt()
yourLetGrade = getLetterGrade(intNumGrade)
yourPlusMinus = getPlusMinus(intNumGrade)
print(f"Your grade is {yourLetGrade}{yourPlusMinus}!")