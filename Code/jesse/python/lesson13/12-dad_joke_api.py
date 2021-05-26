'''
Use the Dad Joke API to get a dad joke and display it to the user. You may want to also use time.sleep to add suspense.

Part 1
Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ with the accept header as application/json. This will return a dad joke in JSON format. You can then use the .json() method on the response to get a dictionary. Get the joke out of the dictionary and show it to the user.

import requests
response = requests.get('https://icanhazdadjoke.com/', headers={'accept': 'application/json'})
print(response.json())

Part 2 (optional)
Add the ability to "search" for jokes by sending an HTTP request to https://icanhazdadjoke.com/search with params containing the search term. Parameters supported by this API are page - which page of results to fetch (default: 1), limit - number of results to return per page (default: 20) (max: 30), and term - search term to use (default: list all jokes). Create a REPL that allows one to enter a search term and go through jokes one at a time. You can also add support for multiple pages. A link to the docs can be found here: https://icanhazdadjoke.com/.

import requests
response = requests.get('https://icanhazdadjoke.com/search', headers={'accept': 'application/json'}, params={'page': 1})
print(response.json())
'''

import requests
response = requests.get('https://icanhazdadjoke.com', headers={'accept': 'application/json'})
response = response.json()

print(f'Your joke: \'{response["joke"]}\'')