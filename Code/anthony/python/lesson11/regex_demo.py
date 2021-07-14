import re

# Match starts at beginning of string
# phone_number = input("Enter a phone number: ")
# if re.match(r'\d{3}-?\d{3}-?\d{4}$', phone_number):
#     print('That is a valid phone number')
# else:
#     print('Invalid format...')

# phone_number = input("Enter phone: ")
# pattern = r'(\d{3}-?\d{3}-?\d{4})$'

# result = re.match(pattern, phone_number)
# phone_num = result.group(1)
# print(phone_num)


# Search, will look anywhere within the sting
# phone_number = input("Enter a phone number: ")
# if re.search(r'\d{3}-?\d{3}-?\d{4}', phone_number):
#     print('That is a valid phone number')
# else:
#     print('Invalid format...')


# phone_number = "123-456-7890 hello"
# pattern = r'(\d{3}-?\d{3}-?\d{4}) \w+'
# results = re.findall(pattern, phone_number)
# print(results)

while True:
    grade = input("Enter your grade: ")
    match = re.match(r'(\d{1,3}).*', grade)
    if match:
        print(f"You entered {grade}")
        grade = match.group(1)
        grade = int(grade)
        if grade > 100:
            print("Invalid grade.")
            continue
        else:
            break
    else:
        print("Invalid grade.")
