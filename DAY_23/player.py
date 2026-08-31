from turtle import Turtle

class Player(Turtle):
    def __init__(self, shape = "turtle"):
        super().__init__(shape)
        self.color("green")
        self.penup()
        self.setheading(90)
        self.initialise()

    def move(self):
        self.forward(10)

    def initialise(self):
        self.goto(0, -280)