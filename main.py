# Imports
from turtle import Turtle, Screen

# Objects
myTurtle = Turtle()
myScreen = Screen()

# Main Program
myTurtle.shape('turtle')
myTurtle.color('red')

n = 4
while n >0 :
    myTurtle.forward(200)
    myTurtle.right(90)
    n-=1


myScreen.exitonclick()
