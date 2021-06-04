"""
Turtle
Explanation
Turtle is a python module that allows us to move a virtual turtle around the screen using programming statements. This turtle has a position and a heading. Below are a list of commands, you can more in the turtle docs.

forward(distance) moves the turtle forward the given number of pixels

left(angle) and right(angle) turns the turtle left or right by the given angle (in degrees)

color(color_name) sets the pen's color, which can be penup() penup() penup()

penup() raises the pen, a line won't be drawn when the turtle moves, pendown() lowers the pen again

setposition(x, y) moves the turtle to the given position

fillcolor(color_name) sets the fill color, begin_fill() indicates you'd like to begin filling in whatever you draw, end_fill() actually fills the shape in.

Use these functions to draw a stick figure with a head, body, two arms, and two legs. Once you're done, go through the examples below and create your own drawing.
"""
from turtle import *
ht()
speed(0)

# Head
circle(50, steps=10000)

# Body
right(90)
forward(250)

# Left leg
right(45)
forward(125)
penup()
back(125)

# Right leg
left(90)
pendown()
forward(125)
penup()
back(125)

# Arms
left(135)
forward(175)
right(90)
pendown()
forward(100)
back(200)

done()
