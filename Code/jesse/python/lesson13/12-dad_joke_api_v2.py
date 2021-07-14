'''
Add the ability to "search" for jokes by sending an HTTP request to https://icanhazdadjoke.com/search with params containing the search term. Parameters supported by this API are page - which page of results to fetch (default: 1), limit - number of results to return per page (default: 20) (max: 30), and term - search term to use (default: list all jokes). Create a REPL that allows one to enter a search term and go through jokes one at a time. You can also add support for multiple pages. A link to the docs can be found here: https://icanhazdadjoke.com/.

import requests
response = requests.get('https://icanhazdadjoke.com/search', headers={'accept': 'application/json'}, params={'page': 1})
print(response.json())
'''

import requests

while True:

    # get search term from user and keep track of the page
    search = input('\nEnter a search term or "q" to quit: ')
    if search != 'q':
        page = 1 
        while True:

            # get response from website
            response = requests.get('https://icanhazdadjoke.com/search', headers={'accept': 'application/json'}, params={'page': page, 'limit': 5, 'term': search})
            response = response.json()

            # print each joke from the response
            for i in range(len(response['results'])):
                print(f'\n{response["results"][i]["joke"]}')

                # offer next joke only if currently displayed joke isn't the last one on the page
                if i != len(response['results']) - 1:
                    next_joke = input('\nPress enter for NEXT JOKE or "q" to quit: ').lower()
                    if next_joke == 'q':
                        quit()  

            # offer to search again if last joke of the last page has been displayed
            if response['current_page'] == response['total_pages']:
                search_again = input('\nEnd of RESULTS. Press enter to SEARCH AGAIN or type "q" to quit: ').lower()
                if search_again == 'q':
                    quit()
                else:
                    break

            # offer to show the next page if the last joke of the current page has been displayed
            # add to page count
            else:
                page += 1
                next_page = input('\nEnd of PAGE. Press enter for NEXT PAGE or type "q" to quit: ').lower()
                if next_page == 'q':
                    quit()
    else:
        quit()