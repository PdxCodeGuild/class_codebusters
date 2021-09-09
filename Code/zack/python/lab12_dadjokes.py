import requests

# page search functionality
page_num = int(input('Which page would you like to look up? '))
max_jokes = int(input('How many jokes would you like between 20 and 30? '))
options = input('Is there a type of joke you are looking for? ')
search_page = {'page': page_num, 'limit': max_jokes, 'term': options, }

# request to site
response = requests.get('https://icanhazdadjoke.com/search',
                        headers={'accept': 'application/json'}, params=search_page)

# site response formatted
jokes = response.json()

# printed result
print(jokes)
