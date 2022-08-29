from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.list_car = []

    def create_car(self):
        random_cars = random.randint(1, 6)
        if random_cars == 1:
            new_car = Turtle("square")
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            y_pos = random.randint(-220, 230)
            new_car.goto(325, y_pos)
            self.list_car.append(new_car)

    def move(self):
        for car in self.list_car:
            car.backward(STARTING_MOVE_DISTANCE)