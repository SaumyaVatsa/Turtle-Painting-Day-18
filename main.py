# Imports
from turtle import Turtle, Screen, colormode
import random

# Objects
myTurtle = Turtle()
myScreen = Screen()

# Main Program
colormode(255)
myTurtle.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spirograph(size):
    for i in range(int(360/size)):
        myTurtle.color(random_color())
        myTurtle.circle(100)
        myTurtle.setheading(myTurtle.heading() + size)


draw_spirograph(5)


myScreen.exitonclick()
