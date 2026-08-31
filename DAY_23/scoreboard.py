from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-295, 265)
        self.score = 0
        self.display()

    def display(self):
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=("Courier", 20, "normal"))

    def inc_score(self):
        self.score += 1
        self.display()

    def game_over(self):
        self.goto(0,-20)
        self.color("red")
        self.write(f"GAME OVER", align="center", font=("Arial", 60, "normal"))


    