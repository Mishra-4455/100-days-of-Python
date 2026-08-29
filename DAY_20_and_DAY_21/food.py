from turtle import Turtle
import random
FOOD_SHAPE = "circle"
FOOD_COLOR = "red"

class Food(Turtle):

    def __init__(self, shape = FOOD_SHAPE):
        super().__init__(shape)
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(FOOD_COLOR)
        self.refresh()

    def refresh(self):
        pos_x = random.randint(-280, 280)
        pos_y = random.randint(-280, 250)
        self.goto(pos_x, pos_y)