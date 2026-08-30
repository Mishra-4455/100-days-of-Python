from turtle import Screen, Turtle
from paddles import Paddles
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
player1 = Paddles()
player2 = Paddles()
ball = Ball()
score = Scoreboard()

screen.bgcolor("black")
screen.setup(width=1200, height=800)
screen.title("Pong Game")
screen.tracer(0)

#The line in the middle of the screen
def versus_line():
    pos = [(0, 360), (0, 300), (0,240), (0,180), (0,120), (0,60), (0, 0), (0, -60), (0, -120), (0, -180), (0, -240), (0, -300), (0, -360), (0, -400)]
    for n in range(0,13):
        versus = Turtle(shape="square")
        versus.color("white")
        versus.penup()
        versus.setheading(90)
        versus.turtlesize(1, 2)
        versus.goto(pos[n])

versus_line()
player2.init_player(580)
player1.init_player(-580)

screen.listen()
screen.onkey(player1.up ,"w")
screen.onkey(player1.down, "s")
screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")
score.display_score()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.02)
    ball.move()

    if ball.ycor() > 390 or ball.ycor() < -390:
        ball.switch_y()

    if (ball.distance(player1) < 50 and ball.xcor() < -560) or (ball.distance(player2) < 50 and ball.xcor() > 560):
        ball.switch_x()    

    if ball.xcor() > 590:
        score.inc_score1()
        ball.rand_start()

    if ball.xcor() < -590:
        score.inc_score2()
        ball.rand_start()

    if score.winning():
        game_on = False
        screen.clear()
        screen.bgcolor("black")
        if score.who() == 1:
            ball.win_display("PLAYER 1")
        elif score.who() == 2:
            ball.win_display("PLAYER 2")



screen.exitonclick()