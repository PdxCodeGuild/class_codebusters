#-----------------------------------------------#
'''
PDX Code Guild
Class CodeBusters
Week 05
Lab 12 - Dad Joke API
Jared Nistler
'''
#-----------------------------------------------#
# Instructions
#-----------------------------------------------#
'''
Part 1
Use the requests library to send an HTTP request to
https://icanhazdadjoke.com/ with the accept header
as application/json. This will return a dad joke
in JSON format. You can then use the .json() method
on the response to get a dictionary. Get the joke
out of the dictionary and show it to the user.

Part 2
Add the ability to "search" for jokes by sending an 
HTTP request to https://icanhazdadjoke.com/search 
with params containing the search term. Parameters 
supported by this API are page - which page of 
results to fetch (default: 1), limit - number of 
results to return per page (default: 20) (max: 30), 
and term - search term to use (default: list all jokes). 
Create a REPL that allows one to enter a search term 
and go through jokes one at a time. You can also add 
support for multiple pages. A link to the docs can be 
found here: https://icanhazdadjoke.com/.

'''
#-----------------------------------------------#
# Developer Notes
#-----------------------------------------------#
'''
Version 1: Complete
Version 2: 

Future Improvements:


'''
#-----------------------------------------------#
# VERSION 1
#-----------------------------------------------#
# Import Dependencies
#-----------------------------------------------#

import requests
import time

#-----------------------------------------------#
# Pull joke from API
#-----------------------------------------------#

def get_joke ():
    response = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
    result_joke = response.json()
    return result_joke['joke']


#-----------------------------------------------#
# User Interface
#-----------------------------------------------#

while True:
    user_input = input("Enter 'Yes' to hear a joke. 'No' to quit: ")
    if user_input == "No":
        break
    elif user_input == "Yes":
        time.sleep(1)
        print(f'''
------------------------------------------------
{get_joke()}
------------------------------------------------
        ''')
    else:
        continue

# #-----------------------------------------------#
# # VERSION 2
# #-----------------------------------------------#
# # Import Dependencies
# #-----------------------------------------------#

# import requests
# import time

# #-----------------------------------------------#
# # Pull jokes from API
# #-----------------------------------------------#

# def get_joke ():
#     response = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
#     result_joke = response.json()
#     return result_joke['joke']

# def search_joke (user_term):
#     response = requests.get('https://icanhazdadjoke.com/search', headers={'accept': 'application/json'}, params={'term': user_term})
#     result_joke = response.json()
#     return result_joke

# #-----------------------------------------------#
# # User Interface
# #-----------------------------------------------#

# while True:
#     user_input = input('''
# Enter a choice:
# 'Yes' to hear a joke. 
# 'Search to make a search'
# 'Quit' to quit.

# ''')
#     if user_input == "Quit":
#         break
#     elif user_input == "Yes":
#         time.sleep(1)
#         print(f'''
# ------------------------------------------------
# {get_joke()}
# ------------------------------------------------
#         ''')
#     elif user_input == "Search":
#         search_term = input("Enter your search term: ")
#         jokes_result = search_joke(search_term)
#         print(f'''
# ------------------------------------------------
# Your search returned {jokes_result['total_jokes']} results
# ------------------------------------------------
#         ''')
        
#     else:
#         continue

