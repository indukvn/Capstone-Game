from turtle import Turtle

STARTING_POSITION = (0, -255)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 250


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(STARTING_POSITION)
        self.shapesize(stretch_wid=1.1, stretch_len=1.1)
        self.left(90)
        self.speed_player = 0.1

    def move(self):
        self.forward(MOVE_DISTANCE)

    def position(self):
        self.goto(STARTING_POSITION)
        self.speed_player *= 0.5
