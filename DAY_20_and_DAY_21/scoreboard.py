from turtle import Turtle
ALLIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_sb()

    def update_sb(self):
        self.goto(0,265)
        self.write(f"Score = {self.score}", False, ALLIGNMENT, FONT)
        self.create_border()

    def create_border(self):
        self.goto(-300,265)
        self.pendown()
        self.goto(300,265)
        self.penup()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_sb()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, ALLIGNMENT, FONT)