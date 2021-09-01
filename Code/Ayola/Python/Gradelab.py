
# Let's convert a number grade to a letter grade, using if and elif statements and comparisons. First have the user enter a number representing the grade (0-100). Then convert the number grade to a letter grade.


# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# 0-59: F


# Ask user to enter no, convert input to int
num_guess = int(input('Enter a number betweeen 1 and 100: '))

if num_guess >= 90:
    print('A')
elif num_guess >= 80:
    print('B')
elif num_guess >= 70:
    print('C')
elif num_guess >= 60:
    print('D')
# use else to catch everything else
else:
    print('D')

# Part 2
# Find the specific letter grade(A+, B-, etc). You can check for more specific ranges using if statements, or use modulus % to get the ones-digit to set another string to '+', '-', or ' '. Then you can concatenate that string with your grade string.

if num_guess >= 96:
    print('A+')
elif num_guess >= 95:
    print('A')
elif num_guess >= 90:
    print('A-')
elif num_guess >= 86:
    print('B+')
elif num_guess >= 85:
    print('B')
elif num_guess >= 80:
    print('B-')
elif num_guess >= 76:
    print('C+')
elif num_guess >= 75:
    print('C')
elif num_guess >= 70:
    print('C-')
elif num_guess >= 66:
    print('D+')
elif num_guess >= 65:
    print('D')
elif num_guess >= 60:
    print('D-')
# use else to catch everything else
else:
    print('F')
