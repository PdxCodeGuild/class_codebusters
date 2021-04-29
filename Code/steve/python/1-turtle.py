'''
Turtle is a python module that allows us to move a virtual turtle around the screen using programming statements. This turtle has a position and a heading. Below are a list of commands, you can more in the turtle docs.

    forward(distance) moves the turtle forward the given number of pixels

    left(angle) and right(angle) turns the turtle left or right by the given angle (in degrees)

    color(color_name) sets the pen's color, which can be penup() penup() penup()

    penup() raises the pen, a line won't be drawn when the turtle moves, pendown() lowers the pen again

    setposition(x, y) moves the turtle to the given position

    fillcolor(color_name) sets the fill color, begin_fill() indicates you'd like to begin filling in whatever you draw, end_fill() actually fills the shape in.

Use these functions to draw a stick figure with a head, body, two arms, and two legs. Once you're done, go through the examples below and create your own drawing.
'''
from turtle import *

# charlie brown you blockhead
left(90)
penup()
forward(200)
pendown()
right(90)
forward(50)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(50)


# look at how slender I am
right(90)
forward(300)

# I can stand
right(45)
forward(150)
penup()
right(180)
forward(150)
right(90)
pendown()
forward(150)

# and my arms
penup()
right(180)
forward(150)
right(45)
forward(150)
pendown()
left(90)
forward(50)
right(45)
forward(50)
penup()
left(180)
forward(50)
left(45)
forward(50)
pendown()
forward(50)
left(45)
forward(50)
penup()

input()
