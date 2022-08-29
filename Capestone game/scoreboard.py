from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.goto(-255, 235)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def next_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.color("white")
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)