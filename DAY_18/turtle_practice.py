from turtle import Turtle, Screen
import random
screen = Screen()
jimmy_the_turtle = Turtle()
jimmy_the_turtle.pensize(5)
screen.colormode(255)

def right_forward():
    jimmy_the_turtle.right(90)
    jimmy_the_turtle.forward(30)

def left_forward():
    jimmy_the_turtle.left(90)
    jimmy_the_turtle.forward(30)

def dashed_line():
    jimmy_the_turtle.penup()
    jimmy_the_turtle.forward(10)
    jimmy_the_turtle.pendown()
    jimmy_the_turtle.forward(10)

def draw_shape(sides):
    for n in range(sides):
        jimmy_the_turtle.forward(100)
        jimmy_the_turtle.right(360/sides)

def random_walk():
    n =  random.randint(0,3)
    if n == 1:
        jimmy_the_turtle.forward(30)
    elif n == 2:
        right_forward()
    elif n == 3:
        left_forward()
    else:
        jimmy_the_turtle.backward(30)

def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    return (r, g, b)

def draw_circle():
    jimmy_the_turtle.circle(100)
    jimmy_the_turtle.left(4)

jimmy_the_turtle.speed(0)
jimmy_the_turtle.pencolor("red")

# for n in range(90):
#     jimmy_the_turtle.color(random_color())
#     draw_circle()

def draw_curve():
    for _ in range(200):
        jimmy_the_turtle.right(1)
        jimmy_the_turtle.forward(2)

jimmy_the_turtle.left(140)
jimmy_the_turtle.forward(224)
draw_curve()

jimmy_the_turtle.left(120)
draw_curve()
jimmy_the_turtle.forward(224)

jimmy_the_turtle.hideturtle()
screen.exitonclick()