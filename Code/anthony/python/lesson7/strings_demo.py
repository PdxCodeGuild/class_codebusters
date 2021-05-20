"This is a string"
'This is also a string'


"""
This is
Also a string
"""

'Coding is "fun"'

"Don't do that"


'Don\'t do that'

"Coding is \"fun\""

# print("\\")
# print("\tsome text")
# print("\nsome more text")
# print(r"\\ \t some text \n some more text")

# print("Hello" + "World")
# print("H" * 50)
# print("H" * "E") # Must be an integer

# print(len("hello"))

greeting = "Hello World"
# print(greeting[4])    # Single will give us character at index
# print(greeting[-1])
# print(greeting[2:8])  # Start and end (exclusive)
# print(greeting[6:])     # Start to end
# print(greeting[6:100:2])    # 3rd number is increment
# print(greeting[6::2])    # 3rd number is increment
# print(greeting[0::1])
# print(greeting[-1::-1])     # String in reverse
# print(greeting[8:4:-1])

# print(greeting.find("l"))
# print(greeting.find("lo"))
# print(greeting.find("coffee"))

# print(greeting.upper())
# print(greeting.lower())
# print(greeting.title())

# print(greeting.startswith('Hello'))
# print(greeting.endswith('x'))
# print(greeting.lower().startswith('he'))
# print(greeting.swapcase())
# split_greeting = greeting.split('l')
# joined_greeting = "m".join(split_greeting)
# print(joined_greeting)

# print(greeting.replace('l', 'm'))


name = "Jerry"
name += " last name"
age = 30
age += 1

# print(f"{name.swapcase()} is {age + 1}")
# print(name + " is " + str(age))

if name not in greeting:
    print(f"Hello {name}")
else:
    print(greeting)


for char in name:
    print(char)
