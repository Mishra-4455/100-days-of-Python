# import colorgram
# palete = colorgram.extract('DOT IMAGE.jpg', 30)
# colours = []
# for n in palete:
#     colours.append(((n.rgb)[0], (n.rgb)[1], (n.rgb)[2]))
# print(colours)

from turtle import Turtle, Screen
import random
screen = Screen()
jimmy_the_turtle = Turtle()
screen.colormode(255)
jimmy_the_turtle.speed(10)
palate = [(204, 164, 107), (155, 73, 46), (235, 238, 244), (52, 92, 123), (224, 201, 135), (171, 153, 40), (138, 31, 21), (132, 162, 185), (200, 91, 71), (48, 122, 87), (14, 99, 73), (95, 73, 75), (146, 178, 147), (72, 47, 38), (163, 142, 158), (234, 175, 165), (55, 46, 50), (184, 206, 172), (19, 85, 90), (144, 21, 24), (41, 62, 74), (82, 145, 128), (181, 87, 89), (41, 66, 90), (13, 71, 68), (213, 178, 183), (179, 191, 207)]

jimmy_the_turtle.hideturtle()
jimmy_the_turtle.penup()
jimmy_the_turtle.right(135)
jimmy_the_turtle.forward(330)
jimmy_the_turtle.left(135)

def walk():
    for n in range(10):
        jimmy_the_turtle.dot(20, random.choice(palate))
        if n != 9:
            jimmy_the_turtle.forward(50)
    
    jimmy_the_turtle.left(90)
    jimmy_the_turtle.forward(50)
    jimmy_the_turtle.left(90)
    jimmy_the_turtle.forward(450)
    jimmy_the_turtle.right(180)
for n in range(0,10):
    walk()

screen.exitonclick()