import requests
import re
import time
exit = False

while not exit: 

    download_all = False
    print('\n\nWelcome to the FOIA library assistant tool.\nYou can supply a search term and I will return a list of links\nto all the available released documents on that topic\nthat are in the Central intelligence agency\'s freedom of information act document library.\n\n   Please note you can require or exclude terms from the search as well using + and -. \n   I.e "+MK ultra" will REQUIRE that "MK" be in the document, not just ultra. \n   This will reduce unwanted links/files.')
    
    search_term = input(f'\nPlease type your search term for the FOIA library: ')
    search_setup = 'https://www.cia.gov/readingroom/search/site/'
    site_response_list = [requests.get(search_setup+search_term).text]
    # this combines our search setup and our search term, then gets the raw HTML text data, saves it to site_response 

    # This will contiually check pages until one shows the default 'Check your spelling' landing page for a bad link
    page = 0
    while True:
        page += 1 # this will increase the page count until failure
        try: 
            extra_page = requests.get(search_setup+search_term+'?page='+str(page)).text
            # this equates to saying https://www.cia.gov/readingroom/search/site/ufo?page=1 for example
            if 'Check if your spelling is correct, or try removing filters.' not in extra_page:
                print(f'\nFound more than one page, adding page #{page}. Press control+c to stop the search at any time.')
                site_response_list.append(extra_page)
            else:
                print(f'\nFound the last page, total pages of data aquired: {pages}')
                break
                
        except:
            print(f'There was an error while trying to check for extra pages, this occured at page #{page}')
            break
    


    site_response_list_converted = ''.join([str(data) for data in site_response_list])
    # this will take our list of strings where each item is a txt version of a whole HTML page and turn it into one long string
    search_links = [x.replace('"', "") for x in re.findall(r'https://www.cia.gov/readingroom/document/.+"' ,site_response_list_converted)]
    # this will find all document links associated with the search from the master string (site_response_list_converted)



    # currently functional selection screen
    while True: 
        if len(search_links) == 0:
            print(f'There were 0 documents matching that search term, please try again')
            break
        else: 
            while True:
                options = input(f'\nThere are approx. {len(search_links)} files matching that description. \n   Would you like to:\n        1) See the links?\n        2) Download the links?\n        3) Search again\n        4) Exit program\n       :')
                try:
                    options = int(options)
                except:
                    print('That was an invalid option, please try again.')
                if options in [1,2,3,4]:
                    break

            if options == 4:
                exit = True
            elif options == 3:
                break
            elif options == 2:
                download_all = True
                print('beginning download...')
                break
            elif options == 1:
                print(f'The following file links are taken from searching the FOIA library for "{search_term}"\n\n')
                for i, link in enumerate(search_links): 
                    print(f'\n    {i+1}) {link}')
                    time.sleep(0.5)

    # currently functional download system
    if download_all == True:
        # this will keep us from downloading a shit load from the CIA's website without need. 
        for i, link in enumerate(search_links):
        # for each link in our search link list, goto the subject page, find the pdf, save it to a file. * 
            print(f'Downloading in progress, currently at: {i/len(search_links)*100}%')
            # this section will take a given link, and find all pdfs within the link, then download them 
            site_response = requests.get(link)
            pdf_list = [x.replace('"', '') for x in re.findall(r'https.+.pdf?"', site_response.text)]
            # this makes a list of the pdf_urls

            for pdf_url in pdf_list: # this loops through the list of URLs and downlaods the pdfs. 
                pdf_data = requests.get(pdf_url)
                print(f"Writing file #{i+1} : {pdf_url}.")
                try:
                    with open(f'./FOI_{search_term}_{pdf_url[-14:-4]}_.pdf', 'wb') as new_file:
                        # this creates a new file, under FOI_searchterm_doc#.pdf
                       new_file.write(pdf_data.content)
                except: 
                    # this will assist in any errors
                    print(f'\n{"*"*50}There was an error downloading file #{i+1}')
        print(f'{"*"*50}\nDownload complete. Thanks for using the FOI assistant.')

