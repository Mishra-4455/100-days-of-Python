from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self, shape = "circle"):
        super().__init__(shape)
        self.color("red")
        self.penup()
        self.x = 5
        self.y = 5
        self.rand_start()

    def rand_start(self):
        r = random.randint(1,3)
        s = random.randint(-300,300)
        self.goto(0, s)
        if r == 1:
            self.x *= -1
        elif r == 2:
            self.y *= -1
        elif r == 3:
            self.y *= -1
            self.x *= -1

    def move(self):
        self.goto(self.xcor()+self.x, self.ycor()+self.y)

    def switch_y(self):
        self.y *= -1
        
    def switch_x(self):
        self.x *= -1

    def win_display(self, play):
        self.goto(0,-20)
        self.color("green")
        self.write(f"{play} WINS !!!", False, "center", ("Arial", 70, "bold"))
        