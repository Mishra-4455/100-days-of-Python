from turtle import Turtle, Screen
import random
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput("Place a Bet", "Which color of turtle do you think is gonna win? ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtles in range(0,6):
    rock = Turtle(shape="turtle")
    rock.color(colors[turtles])
    rock.penup()
    rock.goto(x=-230, y=y_pos[turtles])
    all_turtles.append(rock)
is_running = False

if user_bet:
    is_running = True

while is_running:
    for turtles in all_turtles:
        if turtles.xcor() > 230:
            is_running = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle won.")
            else:
                print(f"You Lost. The {winning_color} turtle won.")
        turtles.forward(random.randint(1,10))

screen.exitonclick()