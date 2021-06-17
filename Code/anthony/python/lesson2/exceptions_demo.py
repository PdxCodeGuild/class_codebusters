
# Types of errors
# if:   # Syntax Error

# if "hello" == True:
#         print("something here")   # Indentation Error
#     print("hello")


# print(x) # Name Error
# x = 5

# x.this_method_is_fake()   # Attribute Error

message = "Greetings everyone!"
# int(message)  # Name Error
# print(x + message)


# Raising Errors
# number = input("Enter a number ")
# if not number.isdigit():
#     raise IndentationError("Number entered must be a digit")  # This will cause a indentation error

# Catching exceptions
# message = input("Enter a number: ")
# try:
#     number = float(message)
# except ValueError:    # We can tell python how we would like to handle the error
#     print("That is not a number")


# message = input("Enter a number: ")
# try:
#     number = float(message)
# except ValueError:    # except runs if specified error gets raised
#     print("That is not a number")
# else:     # else runs if no error
#     print("number converted successfully")
# finally:  # finally runs always
#     print("thanks for trying i guess")


# This is a handy pattern to ensure user enters a valid number
while True:
    message = input("Enter a number: ")
    try:
        number = float(message)
        break
    except ValueError:
        print("Enter a valid number")
    else:
        print("No error occurred")


print(f"Your number is {number}")
