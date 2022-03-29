from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.forward(50)
leo.left(30)
leo.right(40)
done() 

i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(90)
    i = i + 1
