given_dict = {
'a': 1, 
'b': 2
}
def has_key(d, key):
    while True:
        if key in given_dict:
            return True
        else:
            return False