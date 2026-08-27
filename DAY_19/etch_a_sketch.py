from turtle import Turtle, Screen
rock = Turtle()
screen = Screen()

def go_forward():
    rock.forward(10)

def go_backward():
    rock.backward(10)

def turn_left():
    rock.left(10)

def turn_right():
    rock.right(10)

def clear_sc():
    screen.reset()

screen.listen()
while True:
    screen.onkey(go_forward, "w")
    screen.onkey(go_backward, "s")
    screen.onkey(turn_left, "a")
    screen.onkey(turn_right, "d")
    screen.onkey(clear_sc, "c")
    screen.exitonclick()

