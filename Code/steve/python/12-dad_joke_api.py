"""
Dad Joke API

Use the Dad Joke API to get a dad joke and display it to the user. 
You may want to also use time.sleep to add suspense.

Part 1

Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ 
with the accept header as application/json. This will return a dad joke in JSON format. 
You can then use the .json() method on the response to get a dictionary. 
Get the joke out of the dictionary and show it to the user.

import requests
response = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
print(response.json())
"""
import requests
import time



dad_joke = (requests.get('https://icanhazdadjoke.com/',
                         headers={'accept': 'application/json'})).json()

print('Here comes your Dad Joke ....')
time.sleep(3)
print(dad_joke['joke'])
