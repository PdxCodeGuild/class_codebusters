import requests
import time
import json

response = requests.get('https://icanhazdadjoke.com/',
                        headers={'accept': 'application/json'})  # gets joke library
response = response.json()  # converts to dictionary so we can pull just the content
print("I've got a good one for ya......")  # set up
time.sleep(2)  # suspense
print(response["joke"])
