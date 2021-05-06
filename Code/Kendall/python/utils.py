
def get_int(message):
    while True:
        num = input(message)
        try:
            num = int(num)
            if 0 <= num <= 100:
                break
        except ValueError:
            print("Please enter a number. ")
    return num
