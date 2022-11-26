from paddle import Paddle
from ball import Ball
from wall import Wall
from scoreboard import Scoreboard


WALL_TYPES = (
    ("red", 10, 1.8),
    ("orange", 7, 1.6),
    ("yellow", 5, 1.4),
    ("green", 3, 1.2),
    ("blue", 1, 1.0)
)


class GameManager:

    def __init__(self, paddle: Paddle, ball: Ball, scoreboard: Scoreboard):
        self.paddle: Paddle = paddle
        self.ball: Ball = ball
        self.scoreboard = scoreboard
        self.screen_width_boundary = None
        self.screen_height_boundary = None
        self.walls = []
        self.speed_multiplier = 1.0

    def is_ball_touching_vertical_boundary(self):
        return abs(self.ball.xcor()) > self.screen_width_boundary

    def is_ball_touching_top(self):
        return self.ball.ycor() > self.screen_height_boundary

    def is_ball_down_the_bottom(self):
        return self.ball.ycor() < -self.screen_height_boundary

    def is_ball_touching_paddle(self):
        x_offset = 60
        y_offset = 20
        ball_going_down = self.ball.y_move < 0
        b_x, b_y = self.ball.pos()
        p_x, p_y = self.paddle.pos()
        on_same_x_as_paddle = p_x - x_offset <= b_x <= p_x + x_offset
        on_same_y_as_paddle = p_y <= b_y <= p_y + y_offset
        return on_same_y_as_paddle and on_same_x_as_paddle and ball_going_down

    def _is_ball_touching_a_wall(self, wall: Wall):
        ball = self.ball
        return ball.distance(wall) < 30

    def process_wall_touch(self):
        narnia = (self.screen_height_boundary * 2, self.screen_width_boundary * 2)
        for wall in self.walls:
            if self._is_ball_touching_a_wall(wall):
                self.speed_multiplier = wall.speed_multiplier
                self.scoreboard.give_points(wall.value)
                wall.goto(narnia)
                self.walls.remove(wall)
                self.ball.random_bounce()

    def all_walls_were_destroyed(self):
        return len(self.walls) == 0

    def create_walls(self):
        types = WALL_TYPES
        x_start = -self.screen_width_boundary + 45
        y_start = self.screen_height_boundary - 75
        y_pos = y_start
        x_increase, y_decrease = 65, 25
        walls_per_line = 15
        for wall_type in types:
            x_pos = x_start
            for i in range(walls_per_line):
                wall = Wall(wall_type[0], wall_type[1], wall_type[2], (x_pos, y_pos))
                self.walls.append(wall)
                x_pos += x_increase
            y_pos -= y_decrease
