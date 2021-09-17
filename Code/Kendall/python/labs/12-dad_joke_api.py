import json
import requests
import requests
response = requests.get('https://icanhazdadjoke.com/',
                        headers={'accept': 'application/json'})
text = response.json()
print(text['joke'])
