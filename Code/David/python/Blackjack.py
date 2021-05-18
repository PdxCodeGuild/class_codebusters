try:
    first = int(input("whats your first card? "))
except:
    first = a = 1
    first = j = 10
    first = q = 10
    first = k = 10
try:
    second = int(input('whats your second card? '))
except:
    second = 10
try:
    third = int(input('whats your third card? '))
except:
    third = 10
score = first + second + third

if score < 17:
    print(f'{score} "Hit"')
if 21 > score >= 17:
    print(f'{score} "Stay"')
if score == 21:
    print(f'{score} "Blackjack!"')
if score > 21:
    print(f'{score} "Busted"')
