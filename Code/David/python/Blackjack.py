facecards = {'a': 1, 'j': 10, 'q': 10, 'k': 10}
first = (input('whats your first card? '))
if first in facecards:
    first = (facecards[first])
else:
    first = int(first)

second = (input('whats your second card? '))
if second in facecards:
    second = (facecards[second])
else:
    second = int(second)

third = (input('whats your third card? '))
if third in facecards:
    third = (facecards[second])
else:
    third = int(third)


score = first + second + third


if score < 17:
    print(f'{score} "Hit"')
if 21 > score >= 17:
    print(f'{score} "Stay"')
if score == 21:
    print(f'{score} "Blackjack!"')
if score > 21:
    print(f'{score} "Busted"')
