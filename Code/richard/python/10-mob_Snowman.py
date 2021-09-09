# Snowman
# Let's write a program to play a game of Snowman! Snowman is a word game where a secret word is chosen, then players have to guess letters until they get the word correct or they run out of chances and lose.


snowman_pics = [r'''



 (   )
''', r'''


 (   )
 (   )
''', r'''

 (   )
 (   )
 (   )
''', r'''

 (   )
 (   )
 ( : )
''', r'''

 (   )
 ( : )
 ( : )
''', r'''

 ( . )
 ( : )
 ( : )
''', r'''
 _===_
 ( . )
 ( : )
 ( : )
''', r'''
 _===_
 ( .O)
 ( : )
 ( : )
''',r'''
 _===_
 (-.O)
 ( : )
 ( : )
''', r'''
 _===_
 (-.O)
<( : )
 ( : )
''', r'''
 _===_
 (-.O)
<( : )\
 ( : )
''']

for i in snowman_pics:
    print(i)