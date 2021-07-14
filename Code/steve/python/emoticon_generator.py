"""
Let's generate emoticons by randomly choosing a set of eyes, a nose, and a mouth. Examples of emoticons are :-D =^P and :\. You can view a long list on wikipedia.

    Define a list of eyes
    Define a list of noses
    Define a list of mouths
    Randomly pick a set of eyes
    Randomly pick a nose
    Randomly pick a mouth
    Use concatenation to combine them and display the emoticon

Example output:
:-P
"""
import random


eyes = [':', ';', '*', 'X', '%', '8']
nose = ['+', '', '-', '<']
mouths = [')', 'D', '}', 'P', 'O', 'X', ']', '(']


def create_emo():
    return f'{random.choice(eyes)}{random.choice(nose)}{random.choice(mouths)}'


"""
Version 2

Use a while loop to generate 5 emoticons.
"""

# num = 0
# while num < 5:
#     print(f'{random.choice(eyes)}{random.choice(nose)}{random.choice(mouths)}')
#     num += 1


"""
Version 3

Randomly generate vertical emoticons like ^_^ (-_-), [*.*]
"""

v_eyes = ['´', ' ﾟ', '-', '^', 'ー', '0', '◠', 'Ｔ', '=', '≦', '◕']
v_mouth = ['ー', '□', 'ｖ', 'u', 'U', '▽', '・', 'o', 'ω']
v_outer_left = ['m(', '(*', '(／', '(✿', '(=', '<(']
v_outer_left_symetric = [')m', '*)', '\)', '✿)', '=)', ')>']
v_outer_right = ['●)', '*)', ';)', 'b))', ')!!']


def create_vert_emo(option='s'):
    eye = random.choice(v_eyes)
    out_index = random.randint(0, len(v_outer_left))
    if option == 'a':
        return f'{random.choice(v_outer_left)}{eye}{random.choice(v_mouth)}{eye}{random.choice(v_outer_right)}'
    else:
        return f'{v_outer_left[out_index]}{eye}{random.choice(v_mouth)}{eye}{v_outer_left_symetric[out_index]}'


while True:
    while True:
        choice = input(
            'Would you like a horizontal or vertical emoticon? ').title()
        if choice == 'Horizontal' or choice == 'Vertical' or choice == "Done":
            break
        else:
            print(
                f'{choice} was not a valid option.  Please select between Horizontal and Vertical')

    if choice == 'Horizontal':
        print(create_emo())
    elif choice == 'Vertical':
        sym = input('Do you want symetric "s" or asymetric "a"? ').lower()
        print(create_vert_emo(sym))
    else:
        print('See ya!')
        break
