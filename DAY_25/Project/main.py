import pandas
from turtle import Turtle,Screen


turtle = Turtle()
screen = Screen()
current_score = 0
screen.title(f"50/{current_score} USA States Guessing Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

writer = Turtle()
writer.penup()
writer.hideturtle()
states_data = pandas.read_csv("50_states.csv")

while current_score < 50:
    answer_state = (screen.textinput(f"{current_score}/50 States correct", "What's another state's name?")).title()
    data_set = states_data[states_data["state"] == answer_state]

    if answer_state == "Exit":
        break
    if not data_set.empty:
        x_axis = data_set.x.iloc[0]
        y_axis = data_set.y.iloc[0]
        writer.goto(x_axis,y_axis)
        writer.write(f"{answer_state}", align="left", font=("Arial", 8, "normal"))
        current_score += 1

screen.exitonclick()