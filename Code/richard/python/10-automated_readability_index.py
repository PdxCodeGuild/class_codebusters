# The score is computed by multiplying the number of characters divided by the number of words by 4.71, adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. If the result is a decimal, always round up, and if the result is higher than 14, it should be set to 14.
    # Score  Ages     Grade Level
    #  1       5-6    Kindergarten
    #  2       6-7    First Grade
    #  3       7-8    Second Grade
    #  4       8-9    Third Grade
    #  5      9-10    Fourth Grade
    #  6     10-11    Fifth Grade
    #  7     11-12    Sixth Grade
    #  8     12-13    Seventh Grade
    #  9     13-14    Eighth Grade
    # 10     14-15    Ninth Grade
    # 11     15-16    Tenth Grade
    # 12     16-17    Eleventh grade
    # 13     17-18    Twelfth grade
    # 14     18-22    College
import requests
import re
import math

response = requests.get('https://www.gutenberg.org/files/65296/65296-0.txt')
response.encoding = 'utf-8'

words = len(response.text.split(' '))
char = len(list(response.text))
sentences = len(re.split(r' *[\.\?!][\'"\)\]]* *', response.text))

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}


book = "Why We Love Lincoln"
score = math.ceil(((4.71 * (char / words)) + (0.5 * (words / sentences))) - 21.43)
if score >= 14:
    grade = ari_scale[14]['grade_level']
    age = ari_scale[14]['ages']
else:
    grade = ari_scale[score]['grade_level']
    age = ari_scale[score]['ages']


print(f"""The ARI for {book} is {score}
This corresponds to a {grade} level of difficulty
that is suitable for an average person {age} years old.""")