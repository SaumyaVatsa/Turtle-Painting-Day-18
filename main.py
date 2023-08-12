# Imports
from turtle import Turtle, Screen, colormode
import random

# Objects
color_list = [(148, 78, 53), (199, 151, 113), (22, 27, 53), (235, 224, 96), (135, 161, 200), (65, 88, 132), (137, 68, 88), (48, 31, 24), (26, 38, 30), (63, 28, 36), (44, 51, 107), (122, 35, 49), (143, 175, 158), (187, 142, 159), (76, 108, 82), (186, 92, 124), (131, 33, 27), (202, 89, 70), (102, 111, 184), (68, 74, 40), (169, 186, 224), (102, 150, 99), (158, 205, 215), (226, 176, 168), (50, 82, 35), (219, 174, 186)]
myScreen = Screen()
myTurtle = Turtle()


# Main Program
colormode(255)
myTurtle.speed('fastest')
myTurtle.penup()
myTurtle.setheading(225)
myTurtle.forward(300)
myTurtle.setheading(0)
number_of_dots = 100

for dotCount in range(1, number_of_dots+1):
    myTurtle.dot(20, random.choice(color_list))
    myTurtle.forward(50)
    if dotCount % 10 == 0:
        myTurtle.setheading(90)
        myTurtle.forward(50)
        myTurtle.setheading(180)
        myTurtle.forward(500)
        myTurtle.setheading(0)

myScreen.exitonclick()











