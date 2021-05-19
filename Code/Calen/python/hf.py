#----------------------------------------------------#
# *'-.-'*'-.-'(👍≖‿‿≖)👍 👍(≖‿‿≖👍)*'-.-'*'--'*#
# 
#          Module: Handy functions
#          Version: 1.0
#          Author: Calen Ray
#          Email: Calen.w.ray@gmail.com
#          Date: 05/4/21 
#          Last edited: 5/4/21
#
#----------------------------------------------------#

"""
This is my common functions module for importing across class. 
"""





#The get_input function! 

def get_input(input_datatype=str):
    """ This function will allow us to pull any one of three common datatypes via input and check """
    type_list = [int, float, str]
    
    if input_datatype in type_list:
        

        # this one is simple, string 
        if input_datatype == str:
            user_input = input(" | string:  ")
            return user_input
        


        # Slightly more complicated using a float as we have to return a proper float and verify. 
        if input_datatype == float:
            while True:
                user_input = input(" | float:  ")

                try:
                    user_input = float(user_input)
                except:
                    pass

                if type(user_input) == float: 
                    return user_input
                    break # if this is even needed.
                print(f'{user_input} was not a valid input, try to exclude letters or decimal points.')
        

        # integer type input.
        if input_datatype == int:
            while True:
                user_input = input(" | int:  ")

                try:
                    user_input = int(user_input)
                except:
                    pass

                if type(user_input) == int:
                    return user_input
                    break # again if this is even needed? 
                print(f'{user_input} was not a valid input, try to exclude letters')



    else:
        print('Looks like there was an error in the type of input requested by the code.')


# below will utilize the __name__ function to determine if the module is being ran by itself or called upon by another file. 
# the below code will only run in an environment where this is the main file.
# if __name__ == '__main__':
#     print(get_input(int))
#     print(get_input(float))
#     print(get_input(str))

# ---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+--#
#  o   o | o   o | o   o | o   o | o   o | o   o | o   o | o   o | o   o#
# ---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+--#
#  o | o   o | o   o | o   o | o   o | o   o | o   o | o   o | o   o | o#
# ---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+--#



# the list maker!!!! 
# ugh this will be so nice to automate. 

def convert_to_list(string1):
    new_list = []
    for x in string1:
        new_list.append(x)
    return new_list


# if __name__ == '__main__':
#     pass

# ---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+--#
#  o   o | o   o | o   o | o   o | o   o | o   o | o   o | o   o | o   o#
# ---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+--#
#  o | o   o | o   o | o   o | o   o | o   o | o   o | o   o | o   o | o#
# ---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+--#

# why not make a smaller print function and forcibly use f strings and brackets
# damn, it does not work :( you still need to use p(f"")

def p(text):
    return print(f'{text}')


# if __name__ == '__main__':
#     x = 5
#     p('text test with matching quotes{x}')

# ---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+--#
#  o   o | o   o | o   o | o   o | o   o | o   o | o   o | o   o | o   o#
# ---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+--#
#  o | o   o | o   o | o   o | o   o | o   o | o   o | o   o | o   o | o#
# ---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+--#

