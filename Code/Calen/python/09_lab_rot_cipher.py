# set perams.---------------
index_adjustmnet = 0

alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9',]


# get input --------------------------
while True:
    user_input = input('Please advise on rot number: ')
    try:
        user_input = int(user_input)
    
    except ValueError:
        pass

    if type(user_input) == int:
        index_adjustmnet += user_input 
        break

# process input -------------
non_coded_text = list(input(f'please insert your text, rot selected is {index_adjustmnet}:  '))

for i in range(len(non_coded_text)-1):
    if non_coded_text[i] in alph:
        try:
            non_coded_text[i] = alph[i+index_adjustmnet]
        except IndexError:
            temp_index_adjustment = (i+index_adjustmnet)-len(alph)-1
            non_coded_text[i] = alph[temp_index_adjustment]

print(non_coded_text)



