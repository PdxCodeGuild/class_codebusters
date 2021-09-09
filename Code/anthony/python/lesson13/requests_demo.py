from sre_constants import CATEGORY_UNI_LINEBREAK
import requests
import json
import re
import time
import html

# response = requests.get('https://jsonplaceholder.typicode.com/posts')

# posts = response.text
# posts = json.loads(posts)

# print(posts)
# for post in posts:
#     print('title:', post['title'])
#     print('\t', post['body'], '\n')


# url = 'https://or.water.usgs.gov/non-usgs/bes/'
# response = requests.get(url)
# # print(response.text)
# webpage = response.text
# # <td align=center><a href="shipyard.rain">data table</a></td>

# rain_links = re.findall(r'"(\w+\.rain)"', webpage)

# all_data = ''
# for i, data_set in enumerate(rain_links):
#     print(f'Getting {data_set}. {i/len(rain_links) * 100:.2f}% complete')
#     try:
#         response = requests.get(url + data_set)
#         all_data += response.text
#     except:
#         print(f'Failed to get {data_set}.')
#     time.sleep(1)

# with open('./rain_data.txt', 'w+') as file:
#     file.write(all_data)

url = 'https://opentdb.com/api.php'
print("Welcome to the computer quiz!")
number_of_questions = int(input("How many questions do you want? "))
challenge = input("easy/medium/hard? ")

params = {
    'amount': number_of_questions,
    'category': 18,
    'difficulty': challenge,
    'type': 'boolean'
}


response = requests.get(url, params=params)
raw_data = json.loads(response.text)
questions = raw_data['results']
print(response.url)

correct = 0
current = 1
for question in questions:
    print(f"#{current} -- {html.unescape(question['question'])}")
    answer = input("1) True\n2) False\n")
    answer = 'True' if answer == "1" else 'False'
    if question['correct_answer'] == answer:
        correct += 1
        print(f'{correct} Correct!')
    else:
        print('Incorrect :(')
    current += 1

incorrect = len(questions) - correct
print(f'{correct/len(questions) * 100:.2f}%')
