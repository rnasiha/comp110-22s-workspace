"""A beautiful mountain home in the moonlight."""

__author__ = "730330522"
# shapes: triangles, square, rectangles, lines

from turtle import Turtle, done
leo: Turtle = Turtle()


def square(side: float) -> None:
    """Square -> Draw a square, pass side as input parameter."""
    i: int = 0
    while (i < 4):
        leo.forward(side)
        leo.left(90)
        i = i + 1


def rectangle(length: float, height: float) -> None:
    """Rectangle -> Draw a rectangle, pass length and height as input parameters."""
    for i in (1, 2):
        leo.forward(length)
        leo.left(90)
        leo.forward(height)
        leo.left(90)


def line(x: int, y: int, length: int) -> None:
    """Line  -> Draw a line with x y axis, length as input parameter."""
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.forward(length)


def triangle(side: float) -> None:
    """Triangle -> Draw a triangle, pass side as input parameter."""
    for i in (1, 3):
        leo.forward(side)
        leo.left(120)
    leo.forward(side)


def main() -> None:
    """The entrypoint of my scene."""

# Turtle variable -> leo.

# Procedures:
# triangle -> Draw a triangle, pass side as input parameter. 
# square -> Draw a square, pass side as input parameter. 
# rectangle -> Draw a rectangle, pass length and height as input parameters. 
# line  -> Draw a line with x y axis, length as input parameter.


line(-350, -100, 700)

leo.color("purple")

leo.begin_fill()
triangle(200)
leo.end_fill()

leo.penup()
leo.goto(-200, -100)
leo.pendown()
leo.left(120)
leo.begin_fill()
triangle(250)
leo.end_fill()

leo.penup()
leo.goto(-350, -100)
leo.pendown()
leo.left(120)

leo.color("lavender")
leo.begin_fill()
triangle(300)
leo.end_fill()


# house
leo.color("beige")
leo.penup()
leo.goto(90, -100)
leo.pendown()
leo.begin_fill()
leo.left(120)
square(100)
leo.end_fill()


# door
leo.color("gray")
leo.penup()
leo.goto(100, -100)
leo.pendown()
leo.begin_fill()
rectangle(15, 25)
leo.end_fill()


# window 1
leo.color("light blue")
leo.penup()
leo.goto(160, -20)
leo.pendown()
leo.begin_fill()
square(10)
leo.end_fill()

# window 2
leo.penup()
leo.goto(160, -40)
leo.pendown()
leo.begin_fill()
square(10)
leo.end_fill()

# window 3
leo.penup()
leo.goto(160, -60)
leo.pendown()
leo.begin_fill()
square(10)
leo.end_fill()


# moon
leo.penup()
leo.goto(220, 150)
leo.pendown()
leo.color("yellow")
leo.begin_fill()
leo.circle(50)
leo.end_fill()

done()
