import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=700, height=550)
screen.title("Cape Stone Game")
screen.bgcolor("black")
screen.tracer(0)

screen.listen()

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    if player.ycor() > 250:
        player.position()
        scoreboard.next_level()

    for cars in car.list_car:
        if cars.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
