def setup():
    from gamescreen import GameScreen
    from gamemanager import GameManager
    from scoreboard import Scoreboard
    from paddle import Paddle
    from ball import Ball

    screen = GameScreen()
    paddle = Paddle()
    ball = Ball(paddle=paddle)
    scoreboard = Scoreboard()

    manager = GameManager(paddle=paddle, ball=ball, scoreboard=scoreboard)
    screen.register_game_manager(game_manager=manager)
    manager.create_walls()

    return screen, manager, scoreboard, ball, paddle


def main():

    screen, manager, scoreboard, ball, paddle = setup()

    game_is_on = True
    while game_is_on:

        screen.update()
        scoreboard.update()

        ball.move(speed_multiplier=manager.speed_multiplier)

        if manager.is_ball_touching_vertical_boundary():
            ball.bounce_x()

        if manager.is_ball_touching_top() or manager.is_ball_touching_paddle():
            ball.bounce_y()

        manager.process_wall_touch()

        if manager.is_ball_down_the_bottom():
            scoreboard.take_a_life()
            ball.reset_position()

        if scoreboard.lives <= 0 or manager.all_walls_were_destroyed():
            scoreboard.print_game_over()
            game_is_on = False

    screen.update()
    screen.exitonclick()


if __name__ == '__main__':
    main()
