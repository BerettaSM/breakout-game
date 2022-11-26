from turtle import Turtle


class Wall(Turtle):

    def __init__(self, color, value, speed_multiplier, pos=(0, 0)):
        super().__init__()
        self.color(color)
        self.value = value
        self.speed_multiplier = speed_multiplier
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.goto(*pos)
