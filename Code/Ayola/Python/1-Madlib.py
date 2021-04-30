'''
Search the internet for an example Mad Lib.
Ask the user for each word you'll put in your Mad Lib.
Use string concatenation to combine with user input with other strings to form the Mad Lib.
Display the Mad Lib to the user.

'''

# ask user to answer a few question. Use input() function
Doctors = input ("Name any medical specialty: ") 
motive = input ("What motivates you? ") 
scarry= input ("What were you most scared of as a child? ")
animal = input ("Name an animal you fear the most: ")
smile = input ("What makes you happy? ")



#Come up with story using input from above. Use .f for variables
print (f"I`m suing my {Doctors} after a visit where he told me I have {scarry} in my head, which he claimed were caused by {animal} bite. I ended up spending all my life`s savings on {smile}. When I win, I will spend it all on {motive}.")