# Get int module
def get_int(message):
    while True:
        # input score
        num = input(message)
        try:
            num = int(num)
            if 0 <= num <= 100:
                break
        except ValueError:
            print('Enter a valid number: ')
    return num
