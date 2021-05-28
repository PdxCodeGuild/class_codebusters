'''
Part 1
Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ 
with the accept header as application/json. 
This will return a dad joke in JSON format. 
You can then use the .json() method on the response to get a dictionary. 
Get the joke out of the dictionary and show it to the user.

import requests
response = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
print(response.json())
'''

import requests
import re
import time

# format {'id': 'PZDAXL6pOCd', 
#         'joke': 'What was a more important invention than the first telephone? The second one.', 
#          'status': 200}

jokes_given = []
# keeps track of already provided joke

while True:
    # this will let us repeat jokes 

    if len(jokes_given) == 0:
        # this will run if no joke has been provided yet
        run_joke = True if input(f"{'#'*50} \nWelcome to the dad joke game, where we have a good time. \nwould you like to hear a joke? ").lower() in ['yes', 'y', 'yes please'] else False
    else:
        # this will run each time after the first joke was provided 
        run_joke = True if input(f"{'#'*50}\nwould you like to hear another joke?   ").lower() in ['yes', 'y', 'yes please'] else False
    
    if run_joke == False:
        # this breaks the while loop if we enter anything other then a yes/y/yes please
        break
    random = False if input(f'Would you like to find a joke by keyword or random?').lower() in ['key','keyword','k','search'] else True

    if random == True:
        # this will run a random joke
        joke_dic = (requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})).json()
        # this gets us a fresh joke

        while joke_dic in jokes_given:
            #This will refresh the joke if it's one we have already heard
            joke_dic = (requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})).json()
    else: 
        search_term = input(f'What would you like your search term to be?   ')
        
        joke_dic = ((requests.get('https://icanhazdadjoke.com/search?term='+search_term, headers={'accept': 'application/json'}, params={'page': 1})).json())['results']
        if len(joke_dic) > 1:
            index = int(input(f'It would appear there are {len(joke_dic)} options for jokes, default will be #1 unless you have a preference, which would you like? '))
            inex = abs(index) if abs(index) <= len(joke_dic) else 0
            print(f'Running joke #{index} ')
            time.sleep(2)
            joke_dic = joke_dic[index-1]

    jokes_given.append(joke_dic)
    # this will add this joke the roster of jokes we've already heard

    split_joke = re.split(r'[.?!,]', joke_dic['joke'])
    joke_part_one = split_joke.pop(0)
    joke_part_two = ''.join(split_joke)
    # this uses regex to split the joke into a punchline and a lead-up

    print(joke_part_one+',')

    for i in range(3):
        # this uses sleep to add suspense per instructions
        time.sleep(1)
        print('.'*(i+1))
    
    print(joke_part_two)


print(f'Thank you for stopping by.')