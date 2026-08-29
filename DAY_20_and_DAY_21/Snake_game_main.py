from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
GAME_BG = "grey"

screen = Screen()
screen.bgcolor(GAME_BG)
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


game_on = True
while game_on:
    #default function for snake movement
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detects eating food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #detects collision with any of the walls
    if snake.snake_head.xcor() < -280 or snake.snake_head.xcor() > 280 or snake.snake_head.ycor() < -280 or snake.snake_head.ycor() > 260:
        game_on = False
        scoreboard.game_over()

    #detect collision with any of its body parts
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()