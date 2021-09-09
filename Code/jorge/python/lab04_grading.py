# Function to keep numbers valid
while True:
    # input score
    grade = input(f'Please enter your score: ')
    try:
        grade = int(grade)
        if 0 <= grade <= 100:
            break
    except ValueError:
        print('Enter a valid number: ')
# comparison
if grade >= 98 or grade == 100:
    print('A+')
elif grade >= 93 and grade <= 97:
    print('A')
elif grade >= 90 and grade <= 92:
    print('A-')
elif grade >= 87 and grade <= 89:
    print('B+')
elif grade >= 84 and grade <= 86:
    print('B')
elif grade >= 80 and grade <= 83:
    print('B-')
elif grade >= 77 and grade <= 79:
    print('C+')
elif grade >= 74 and grade <= 76:
    print('C')
elif grade >= 70 and grade <= 73:
    print('C-')
elif grade >= 60:
    print('D')
else:
    print('F')
