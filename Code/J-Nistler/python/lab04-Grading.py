#-----------------------------------------------#
'''
PDX Code Guild
Class CodeBusters
Week 02
Lab 04 - Grading
Jared Nistler
'''
#-----------------------------------------------#
# Instructions
#-----------------------------------------------#
'''
Let's convert a number grade to a letter grade, 
using if and elif statements and comparisons. 
First have the user enter a number representing 
the grade (0-100). Then convert the number grade 
to a letter grade.
'''
#-----------------------------------------------#
# Developer Notes
#-----------------------------------------------#
'''
Version 1: Complete
Version 2: Complete

Future Improvements:

- Validate user input to only include a numerical value between
1-100

'''

#-----------------------------------------------#
# User Input
#-----------------------------------------------#

# Solicit user input
user_input = input("Enter your numeric grade: ")
user_input = int(user_input)

#-----------------------------------------------#
# Convert Grade
#-----------------------------------------------#

'''
Takes in an int as an argument and returns the 
cooresponding letter grade as a string
'''
def calc_grade (num):
    if num >= 90:
        user_grade = "A"
    elif num >= 80:
        user_grade = "B"
    elif num >= 70:
        user_grade = "C"
    elif num >= 60:
        user_grade = "D"
    else:
        user_grade = "F"
    return user_grade

'''
Takes in an int as an argument and returns the 
cooresponding grade modifier(+,- or nothing) as a string
##A grade lower than 59 does not get a modifer##
'''
def calc_modifier (num):
    if num > 59 and (num%10) > 7:
        user_mod = "+"
    elif num > 59 and (num%10) < 3:
        user_mod = "-"
    else:
        user_mod = " "
    return user_mod

#-----------------------------------------------#
# Print Result
#-----------------------------------------------#

print(f"You received a score of {user_input}, which is the letter grade {calc_grade(user_input)}{calc_modifier(user_input)}")