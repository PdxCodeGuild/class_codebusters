'''
Let's convert a number grade to a letter grade, using if and elif statements and comparisons. 
First have the user enter a number representing the grade (0-100). 
Then convert the number grade to a letter grade.

Concepts Covered:
fundamentals, comparisons & conditionals
Numeric Ranges:

90-100: A
80-89: B
70-79: C
60-69: D
0-59: F

97-100 A+
93-96 A
90-92 A-
87-89 B+
83-86 B
80-82 B-
77-79 C+
73-76 C
70-72 C-
67-69 D+
65-66 D
Below 65 F

'''
# # user inputs a number grade from 0 to 100
# user_input = input('Enter a grade: ')

# # convert string to integer
# grade = int(user_input)

# # comparison statements for letter grades
# if grade > 90:
#     print('A')
# elif grade >= 80 and grade <= 89:
#     print('B')
# elif grade >= 70 and grade <= 79:
#     print('C')
# elif grade >= 60 and grade <= 69:
#     print('D')
# else:
#     print('F')


# user inputs a number grade from 0 to 100
user_input = input('Enter a grade: ')
# convert string to integer
grade = int(user_input)
# comparison statements for letter grades
if grade >= 97:
    print('A+')
elif grade >= 93 and grade <= 96:
    print('A')
elif grade >= 90 and grade <= 92:
    print('A-')
elif grade >= 87 and grade <= 89:
    print('B+')
elif grade >= 83 and grade <= 86:
    print('B')
elif grade >= 80 and grade <= 82:
    print('B-')
elif grade >= 77 and grade <= 79:
    print('C+')
elif grade >= 73 and grade <= 76:
    print('C')
elif grade >= 70 and grade <= 72:
    print('C-')
elif grade >= 67 and grade <= 69:
    print('D+')
elif grade >= 65 and grade <= 66:
    print('D')
else:
    print('F')
