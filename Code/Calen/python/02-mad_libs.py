#----------------------------------------------------#
# *'-.-'*'-.-'(👍≖‿‿≖)👍 👍(≖‿‿≖👍)*'-.-'*'--'*#
# 
#          Project: Python mad-labs (get it?)
#          Version: 1.0
#          Author: Calen Ray
#          Email: Calen.w.ray@gmail.com
#          Date: 04/28/21
#----------------------------------------------------#

ok_options = ['start over', 'again', 'read', 'play', 'exit', 'stop']
banner = '*'*75
play_count = 0

#----------------------------------------------------#

# the questions section  

while True:
    if play_count == 0:
        option = 'start over' 
    if option == 'start over' or option == 'again':
        holiday = input("What is your favorite holiday? - ")
        noun = input("A noun please:  ")
        place = input("Name a place:  ")
        person = input("Name public figure or famous perosn:  ")
        adjective = input("An adjective please:  ")
        body = input("Name the first body part that comes to mind:  ")
        verb = input("A verb please:  ")
        adjective_1 = input("Another adjective please:  ")
        noun_1 = input("Another noun please:  ")
        print("We are nearly done, just a bit more...")
        food = input("Your least favorite food?  ")
        noun_plural = input("Please provide a plural noun") 

    # this allows us to handle answers from user without the need for error checking, looping until we fit the criteria.
    while True:
        print(banner)
        option = input(f'Thank you for your help, would you like to read the madlib, start over, or exit? \n please type start over, read, or exit.')
        if option in ok_options:
            break
        else:
            print(f'{banner} \n {option} was not a valid option. please select from the following {ok_options}.')

    if option == 'stop' or option == 'exit':
        print('Thank you for playing, have a nice day.')
        break

    #----------------------------------------------------#

    # the text if ok'd
    if option == 'play' or option == 'read':
        print(f"""

        I can't believe it's already {holiday}! 
        I can't wait to put on my {noun} and visit every {place} in my neighborhood. 
        This year I am going to dress up as (a) {person} with (a) {adjective} {body}. 
        Before I {verb}, I make sure to grab my {adjective_1} {noun_1} to hold all of my {food}.
        Finally, all my {noun_plural} are ready to go!

        """)

    play_count += 1

    #----------------------------------------------------#