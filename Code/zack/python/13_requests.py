import requests

# page search functionality
search = int(input('Which page would you like to look up? '))
search_page = {'page': search}

# request to site
response = requests.get('https://icanhazdadjoke.com/search',
                        headers={'accept': 'application/json'}, params=search_page)

# site response formatted
jokes = response.json()
print(jokes)
# limiting number of jokes
# a list of total jokes taken from the page
joke_list = jokes['results']
# number of jokes per page
joke_nums = int(input("How many jokes would you like(20-30)? "))
# the new list to be scaled down
joking = []
# joke counter
jokes = 0
# looping through the list of jokes adding a joke at a time
while jokes < joke_nums:
    joking.append(joke_list[jokes])
    jokes += 1


# printing the new list of jokes
print(joking)
