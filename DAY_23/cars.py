from turtle import Turtle
import random
COLORS = ["red", "orange", "blue", "yellow", "white", "black", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREASE = 10

class Cars:
    def __init__(self):
        self.all_cars = []
        
    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid= 1,stretch_len= 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-250,250)
            new_car.goto(300, new_y)
            self.all_cars.append(new_car)   

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(STARTING_MOVE_DISTANCE)

    def difficulty_inc(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREASE

    def check_collision(self, player):
        for cars in self.all_cars:
            if player.distance(cars) < 20:
                return True
    