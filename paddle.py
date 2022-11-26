from turtle import Turtle


STEPS = 20
STRETCH_LEN = 7


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("cyan")
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=STRETCH_LEN)
        self.width_offset = STRETCH_LEN * 10
        self.screen_limit_left = None
        self.screen_limit_right = None

    def move_left(self):
        new_y_coord = self.xcor() - STEPS
        if new_y_coord >= self.screen_limit_left + self.width_offset:
            self.goto(self.xcor() - STEPS, self.ycor())

    def move_right(self):
        new_y_coord = self.xcor() + STEPS
        if new_y_coord <= self.screen_limit_right - self.width_offset:
            self.goto(self.xcor() + STEPS, self.ycor())
