from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = Cars()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #generating cars
    cars.create_car()
    cars.move_cars()

    #level up condition
    if player.ycor() > 280:
        scoreboard.inc_score()
        cars.difficulty_inc()
        player.initialise()

    #crashing condition
    if cars.check_collision(player):
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()