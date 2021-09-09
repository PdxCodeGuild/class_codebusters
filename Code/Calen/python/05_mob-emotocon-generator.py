#----------------------------------------------------#
# *'-.-'*'-.-'(👍≖‿‿≖)👍 👍(≖‿‿≖👍)*'-.-'*'--'*#
# 
#          Project: Python emotocon generator
#          Version: 1.0
#          Author: Calen Ray
#          Email: Calen.w.ray@gmail.com
#          Date: 04/30/21
#----------------------------------------------------#

import random
import string
from random import choice as everyday_im_shuffling


existing_emotocon_list = [
    '(>_<)',
    '(>_<)>',
    '('')',
    '(^^ゞ',
    '(^_^;)',
    '(-_-;)',
    '(~_~;)',
    '(・.・;)',
    '(・_・;)',
    '(・・;)',
    ' ^^',
    ';^_^;',
    '(#^.^#)',
    '(^^;)',
    '(^.^)',
    '-.o',
    '(-.-)',
    '(-_-)zzz',
    '(^_-)',
    '(^_-)-☆',
    '((+_+))',
    '(+o+)',
    '(°°)',
    '(°-°)',
    '(°.°)',
    '(°_°)',
    '(°_°>)',
    '(°レ°)',
    '(o|o)',
    '<(｀^´)>',
    '^_^',
    '(^_^)',
    '/(^O^)',
    '／(^o^)／',
    '(≧∇≦)/',
    '(/◕ヮ◕)/',
    '(^o^)丿',
    '∩(·ω·)∩',
    '(·ω·)',
    '^ω^',
    '(__)_',
    '(._.)__',
    '(_^_)_',
    '<(_ _)> ',
    '<m(__)m>',
    'm(__)m',
    'm(_ _)m',
    '＼(°ロ＼)',
    '(／ロ°)／',
    '('')',
    '(/_;)',
    '(T_T)',
    '(;_;)',
    '(Ｔ▽Ｔ)',
    '(ー_ー)!!',
    '(-.-)',
    '(-_-)',
    '(一一)',
    '(；一_一)',
    '(=_=)',
    '(=^・^=)',
    '(=^・・^=)',
    '=^_^=',
    '(..)',
    '(._.)',
    '^m^',
    '(?_?)',
    '(－‸ლ)',
    '>^_^<',
    '*^_^*）',
    '§^.^§',
    '(^^ゞ',
    '(p_-)',
    '((d[-_-]b))',
    '(-"-)',
    '(ーー゛)',
    '(^_^メ)',
    '(-_-メ)',
    '(~_~メ)',
    '(－－〆) ',
    '(・へ・)',
    '(^0_0^)',
    '( ..)φφ(..)',
    '(●＾o＾●)',
    '(＾ｖ＾)',
    '(＾ｕ＾)',
    '(＾◇＾) ',
    '(*^▽^*)',
    '(✿◠‿◠)',
    '(￣ー￣)',
    '(￣□￣;)',
    '(*´▽｀*)',
]

eyes = ['=', ':', ';']
nose = ['+', '', '-', '<']
mouth = [')', '(', '|', 'P', '{', '[']

v_eyes = ['´', ' ﾟ', '-', '^', 'ー', '0', '◠', 'Ｔ', '=', '≦', '◕']
v_mouth = ['ー', '□', 'ｖ', 'u', 'U', '▽', '・', 'o', 'ω']
v_outer_left = ['m(', '(*', '(／', '(✿', '(=', '<(']
v_outer_right = ['●)','*)',';)','b))',')!!']


while True: # This lets us loop to continue to offer to generate an emotocon 

    while True:
        choice = input('Would you like to generate a vertical or horizontal emotocon?\n Horizontal, Vertical, Random, or Done:   ').title  () 

        if choice == 'Horizontal' or choice == 'Vertical' or choice == 'Done' or choice == 'Random':
            break
        else:
            print(f'{choice} was not a valid option, please select from Horizontal, Vertical, or Done.')
        
    
    if choice == 'Vertical':
        # I f-ing hate myself for calling the random.choice() function everyday_im_shuffling, its brain damage to use irl. 
        print(f'''your new vertical emotocon is: 

        {everyday_im_shuffling(v_outer_left)}{everyday_im_shuffling(v_eyes)}{everyday_im_shuffling(v_mouth)}{everyday_im_shuffling(v_eyes)}{everyday_im_shuffling(v_outer_right)}
        ''')

    if choice == 'Horizontal':
         print(f'''your new horizontal emotocon is: 

        {everyday_im_shuffling(eyes)}{everyday_im_shuffling(nose)}{everyday_im_shuffling(mouth)}
        ''')
    if choice == 'Random':
        print(f'''your new horizontal emotocon is: 

        {everyday_im_shuffling(existing_emotocon_list)}
        ''')

    if choice == 'Done':
        print('Thank you for playing, have a great day.')
        break