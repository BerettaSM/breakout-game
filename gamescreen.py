from time import sleep
from turtle import Screen

from gamemanager import GameManager

WIDTH = 1000
HEIGHT = 700


class GameScreen:

    def __init__(self):
        self.screen = Screen()
        self.screen.title("Breakout Game")
        self.screen.bgcolor("black")
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.tracer(0)
        self.game_manager: GameManager = None
        self.updates_checked = False

    def exitonclick(self):
        self.screen.exitonclick()

    def update(self):
        if not self.updates_checked:
            self._update_requirement_checks()
        sleep(0.03)
        self.screen.update()

    def register_game_manager(self, game_manager: GameManager):
        self.game_manager = game_manager
        self.game_manager.screen_width_boundary = WIDTH // 2
        self.game_manager.screen_height_boundary = HEIGHT // 2
        self._register_paddle(paddle=self.game_manager.paddle)
        self._position_score()

    def _register_paddle(self, paddle):
        limit = WIDTH // 2
        paddle.screen_limit_left = -limit
        paddle.screen_limit_right = limit
        self._position_paddle()
        self._delegate_command()

    def _delegate_command(self):
        self.screen.listen()
        self.screen.onkeypress(self.game_manager.paddle.move_left, "Left")
        self.screen.onkeypress(self.game_manager.paddle.move_right, "Right")

    def _position_paddle(self):
        self.game_manager.paddle.goto(x=0, y=(-HEIGHT // 2) + 20)

    def _position_score(self):
        x = -WIDTH * .5 + 185
        y = HEIGHT // 2 - 50
        self.game_manager.scoreboard.goto(x, y)

    def _update_requirement_checks(self):
        if self.game_manager is None:
            raise ValueError('Register a game manager through .register_game_manager() method.')
        self.updates_checked = True
