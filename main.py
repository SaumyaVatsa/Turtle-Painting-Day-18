# Imports
from turtle import Turtle, Screen

# Objects
myTurtle = Turtle()
myScreen = Screen()

# Main Program
myTurtle.shape('turtle')
myTurtle.color('red')

def shape(angle, color, n):
    myTurtle.color(color)
    while n > 0:
        myTurtle.forward(100)
        myTurtle.right(angle)
        n -= 1

myTurtle.forward(100)
myTurtle.right(120)
myTurtle.forward(100)
myTurtle.right(120)
shape(90, 'yellow', 4)
shape(72, 'pink', 5)
shape(60,'blue',6)
shape(51.4, 'red', 7)
shape(45, 'purple', 8)
shape(40, 'green', 9)
shape(36, 'black', 10)

myScreen.exitonclick()
