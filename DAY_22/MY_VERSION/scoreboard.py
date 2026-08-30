from turtle import Turtle
WINNING_SCORE = 5

class Scoreboard:
    def __init__(self):
        self.counter = Turtle()
        self.counter.penup()
        self.counter.hideturtle()
        self.counter.color("yellow")
        self.s1 = 0
        self.s2 = 0

    def display_score(self):
        self.counter.clear()
        self.counter.goto(-100, 315)
        self.counter.write(f"{self.s1}", False, "center", ("Arial", 55, "normal"))
        self.counter.goto(100, 315)
        self.counter.write(f"{self.s2}", False, "center", ("Arial", 55, "normal"))

    def inc_score1(self):
        self.s1 += 1
        self.display_score()

    def inc_score2(self):
        self.s2 += 1
        self.display_score()

    def winning (self):
        if self.s1 == WINNING_SCORE or self.s2 == WINNING_SCORE:
            return True
        else:
            return False        

    def who (self):
        if self.s1 == WINNING_SCORE:
            return 1
        elif self.s2 == WINNING_SCORE:
            return 2
        else:
            return 0
    