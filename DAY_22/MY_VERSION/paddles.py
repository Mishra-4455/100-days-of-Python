from turtle import Turtle
LENGTH_OF_PADDLE = 5

class Paddles(Turtle):
    def __init__(self, shape = "square"):
        super().__init__(shape)
        self.color("white")
        self.penup()
        self.turtlesize(1,LENGTH_OF_PADDLE)

    def init_player(self,x):
        self.setheading(90)
        self.goto(x,0)

    def up(self):
        if self.ycor() < 360:
            self.forward(20)
            self.screen.update()


    def down(self):
        if self.ycor() > -360:
            self.backward(20)
            self.screen.update()
        