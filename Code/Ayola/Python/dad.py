import requests
response = requests.get('https://icanhazdadjoke.com/',
                        headers={'accept': 'application/json'})
msg = response.json()
print("DAD JOKE: ", msg['joke'])
