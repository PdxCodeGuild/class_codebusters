
def get_int(message, min=0, max=105):
    while True:
        num = input(message)
        try:
            num = int(num)
            if min <= num <= max:
                break
        except ValueError:
            print("You must enter a valid integer.")
    return num


def get_float():
    ...


def test_module():
    ...


if __name__ == "__main__":
    test_module()
