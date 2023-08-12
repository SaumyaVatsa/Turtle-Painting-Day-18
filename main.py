# Imports
from turtle import Turtle, Screen

# Objects
myTurtle = Turtle()
myScreen = Screen()

# Main Program
myTurtle.shape('turtle')
myTurtle.color('red')
myTurtle.left(45)
myTurtle.forward(200)
n=6
while n>0:
    myTurtle.left(30)
    myTurtle.forward(40)
    n -= 1
myTurtle.right(90)
myTurtle.forward(40)
m = 5
while m>0:
    myTurtle.left(30)
    myTurtle.forward(40)
    m-=1
myTurtle.left(27)
myTurtle.forward(180)


myScreen.exitonclick()
