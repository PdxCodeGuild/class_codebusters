#-----------------------------------------------#
# PDX Code Guild
# Class CodeBusters
# Week 01
# Lab 01
# Jared Nistler
#-----------------------------------------------#

# Import dependencies
from turtle import *

# Draw Left Leg
left(65)
forward(100)

# Draw Right Leg
right(130)
forward(100)

# Return to Hips
penup()
right(180)
forward(100)

# Draw Body
pendown()
right(25)
forward(100)

# Draw Right Arm
right(130)
forward(100)

# Return to Body
penup()
right(180)
forward(100)

# Draw Left Arm
pendown()
left (85)
forward(100)

# Return to Neck
penup()
left(180)
forward(100)

# Draw Head
pendown()
right(25)
circle(50)

# Hide the Turtle Once Complete
hideturtle()

# Prompt user to end the program
input("Press enter once you are done looking at this glorious stick person")
