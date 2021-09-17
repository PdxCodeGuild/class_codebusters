import spacy
import string

ari_scale = {
    1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
    2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
    3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
    4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
    5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
    6: {'ages': '10-11', 'grade_level':    '5th Grade'},
    7: {'ages': '11-12', 'grade_level':    '6th Grade'},
    8: {'ages': '12-13', 'grade_level':    '7th Grade'},
    9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

# Used spaCy to to tokenize the text
nlp = spacy.load('en_core_web_sm')
doc = nlp('Text me dude! I need to talk to you.')


# Get number of sentences from the text
sentences = int(len(list(doc.sents)))
# print(sentences)

# Get number of words from the text
words = 0
word_lst = []
punctuation = list(string.punctuation)
for sentence in doc.sents:
    words += len(sentence)
    for token in sentence:
        if token.lemma_ in punctuation:
            words -= 1
        else:
            word_lst.append(token)
# print(words)

# Get number of characters from the text
characters = 0
for word in word_lst:
    # print(word, len(word))
    characters += len(word)
# print(characters)

# Get ARI score
ari = (4.71 * (characters / words)) + (0.5 * (words / sentences)) - 21.43
ari = round(ari)
if ari > 14:
    ari = 14
elif ari < 1:
    ari = 1
else:
    ari = ari

# Get corresponding age level and grade level
age_level = ari_scale[ari]['ages']
grade_level = ari_scale[ari]['grade_level']

print(
    f'The ARI for the text is {ari}. This corresponds to a {grade_level} level of difficulty that is suitable for an average person {age_level} years old.')
