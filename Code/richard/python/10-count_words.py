# Take the following steps to build up our dictionary. The result should look something like 
# {'a': 3, 'the': 4}

# Make everything lowercase, strip punctuation, split into a list of words.
# Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet,
#  add it with a count of 1. If it is, increment its count.
# Print the most frequent top 10 out with their counts. You can do that with the code below.

import requests
response = requests.get('https://www.gutenberg.org/files/65296/65296-0.txt')
response.encoding = 'utf-8' # set encoding to utf-8
def book_to_list():
    wordList = (response.text.split(' '))
    for i in range(len(wordList)):
        wordList[i] = wordList[i].lower()
        if len(wordList[i]) > 0:
            for j in range(len(wordList[i])):
                    if (wordList[i][j] < 'a') or (wordList[i][j] > 'z'):
                        wordList[i] = wordList[i].replace(wordList[i][j],' ')
    return wordList

def count_words(list_of_words):
    word_dict = {}
    for i in list_of_words:
        i = i.strip()
        if i in word_dict.keys():
            word_dict[i] += 1
        else:
            word_dict[i] = 1
    return word_dict

def findMaxWord(wordDict):
    maxValue = 0
    maxWord = ''
    for i in wordDict:
        if wordDict[i] > maxValue:
            maxValue = wordDict[i]
            maxWord = i
    return maxWord
print(book_to_list())
# print(findMaxWord(count_words(book_to_list())))

