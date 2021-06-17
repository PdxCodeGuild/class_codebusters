# create grading function


# user grade
grade = input('What was your score?: ')
#convert to integer 
grade = int(grade)

#grades
if grade >= 90:
    letter_grade = 'A'
elif grade >= 80:
    letter_grade = 'B'
elif grade >= 70:
    letter_grade = 'C'
elif grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

#grade modifier
if grade % 10 <=3:
    true_grade = letter_grade + '-'
elif grade % 10 <= 6:
    true_grade = letter_grade
elif grade % 10 <= 9:
    true_grade = letter_grade + '+'
print(true_grade)