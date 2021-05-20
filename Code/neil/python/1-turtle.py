'''

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

Examples

Drawing a Square

from turtle import *

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)

done()
Filling in a Square

from turtle import *

fillcolor('red')
begin_fill()

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)

end_fill()

done()
Drawing a Star

from turtle import *

forward(100)
right(144)
forward(100)
right(144)
forward(100)
right(144)
forward(100)
right(144)
forward(100)

done()
Drawing a Square with a Loop

from turtle import *

i = 0
while i < 4:
    forward(100)
    left(90)
    i = i + 1

done()
Drawing a Staircase

from turtle import *

i = 0
while i < 4:    
	forward(100)
	left(90)
	forward(100)
	right(90)
	i = i + 1
done()
Filling in a Square

from turtle import *

fillcolor('red')
begin_fill()

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)

end_fill()

done()
Draw an N-Sided figure

from turtle import *

edge_length = 100
n_sides = 5

i = 0
while i < n_sides:
	forward(edge_length/n_sides)
	right(360/n_sides)
	i = i + 1

done()
8-Sided Spiral

from turtle import *

fillcolor('blue')

n_sides = 8
edge_length = 0

i = 0
begin_fill()
while i < 150:
	forward(edge_length)
	right(360/n_sides)
	i = i + 1
	edge_length = edge_length + 1
end_fill()
done()
Expanding Star

from turtle import *

edge_length = 0
i = 0
while i < 100:
	forward(edge_length)
	right(144)

	edge_length += 4

done()

'''

from turtle import *


# Create a 'circle' for the head
home()
position()
heading()
circle(50)
position()
heading()
circle(120, 1)
position()
heading()

# Lift up pen and put pen down to draw 'line' down for the main body

penup()
pendown()
right(90)
forward(100)

# Create the right leg

right(45)
forward(100)
penup()
setposition(4, -100)

# Create the left leg

pendown()
left(90)
forward(100)

# Create right arm

penup()
setposition(1, -50)
pendown()
right(140)
forward(90)

# Create left arm

penup()
setposition(1, -50)
pendown()
right(165)
forward(90)

# hide turtle aka arrow/pointer
ht()
done()
