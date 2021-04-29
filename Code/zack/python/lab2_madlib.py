#imports
import random


#loop
prompt = "yes"
while prompt == "yes":
#mad lib questions
    place = input("where would you like to go?: ")
    things = input("what three things would you like to do?: ")
    people = input("who would you like to go with?: ")

#mad lib split
    thing = things.split()

#mad lib randomize
    thing = random.choice(thing)
    
#mad lib concatination
    concat = "You wish you were in" + " " + place + " " + thing + " " + "with" + " " + people + "."

#mad lib display
    print(concat)

#finish loop
    prompt = input("would you like to try again yes or no?: ")