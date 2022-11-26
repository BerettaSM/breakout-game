from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3

    def update(self):
        self.clear()
        score_string = f"Lives - {self.lives} | Score - {self.score}"
        self.write(score_string, align=ALIGNMENT, font=FONT)

    def give_points(self, points):
        self.score += points
        self.update()

    def take_a_life(self):
        self.lives -= 1
        self.update()

    def print_game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
