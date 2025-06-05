from turtle import Screen
import scoreboard
import paddle
import ball
from pong_court import Court
import time

screen = Screen()
screen.title("Pong")
screen.setup(width = 800, height = 600)
screen.tracer(0)
screen.bgcolor("black")
screen.listen()

court = Court()
game_ball = ball.Ball()
left_score = scoreboard.Scoreboard(scoreboard.LEFT_SB_POS)
right_score = scoreboard.Scoreboard(scoreboard.RIGHT_SB_POS)
left_paddle = paddle.Paddle(paddle.LEFT_POS)
right_paddle = paddle.Paddle(paddle.RIGHT_POS)

# screen.update()

screen.onkeypress(left_paddle.start_up, "w")
screen.onkeyrelease(left_paddle.stop_up, "w")
screen.onkeypress(left_paddle.start_down, "s")
screen.onkeyrelease(left_paddle.stop_down, "s")
screen.onkeypress(right_paddle.start_up, "Up")
screen.onkeyrelease(right_paddle.stop_up, "Up")
screen.onkeypress(right_paddle.start_down, "Down")
screen.onkeyrelease(right_paddle.stop_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.08)
    left_paddle.move()
    right_paddle.move()

    if not game_ball.is_right and not game_ball.is_left:
        game_ball.serve_ball()

    if game_ball.xcor() > 350:
        right_score.score += 1
        right_score.refresh()
        game_ball.home()
    elif game_ball.xcor() < -350:
        left_score.score =+ 1
        right_score.refresh()
        game_ball.home()

    if game_ball.ycor() >= 290:
       new_heading = game_ball.heading() + 45
       game_ball. seth(new_heading)
    elif game_ball.ycor() <= -290:
       new_heading = game_ball.heading() - 45
       game_ball. seth(new_heading)

    if game_ball.distance(left_paddle) < 15:
        game_ball.back(ball.MOVE_DISTANCE)

screen.exitonclick()

# py main.py
