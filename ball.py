from turtle import Turtle
from random import randint

from paddle import Paddle


STEPS = 10


class Ball(Turtle):

    def __init__(self, paddle: Paddle):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.resizemode(rmode='user')
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.penup()
        self.y_move = None
        self.x_move = None
        self.paddle: Paddle = paddle
        self.reset_position()

    def move(self, speed_multiplier):
        x_speed = self.x_move * speed_multiplier
        y_speed = self.y_move * speed_multiplier
        self.goto(self.xcor() + x_speed, self.ycor() + y_speed)

    def reset_position(self):
        self.y_move = STEPS
        self.x_move = STEPS if randint(0, 1) == 1 else - STEPS
        self.goto(x=0, y=0)

    def speed_up(self):
        pass

    def random_bounce(self):
        self.bounce_y()
        if randint(0, 1) == 1:
            self.bounce_x()

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
