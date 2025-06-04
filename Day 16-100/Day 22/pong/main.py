from turtle import Screen
import scoreboard
import paddle
from ball import Ball
from pong_court import Court
import time

screen = Screen()
screen.title("Pong")
screen.setup(width = 800, height = 600)
screen.tracer(0)
screen.bgcolor("black")
screen.listen()

court = Court()
ball = Ball()
left_score = scoreboard.Scoreboard(scoreboard.LEFT_SB_POS)
right_score = scoreboard.Scoreboard(scoreboard.RIGHT_SB_POS)
left_paddle = paddle.Paddle(paddle.LEFT_PADDLE_POS)
right_paddle = paddle.Paddle(paddle.RIGHT_PADDLE_POS)

screen.update()

screen.onkeypress(left_paddle.start_up, "Up")
screen.onkeyrelease(left_paddle.stop_up, "Up")
screen.onkeypress(left_paddle.start_down, "Down")
screen.onkeyrelease(left_paddle.stop_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    left_paddle.move()
    ball.serve_left()
    screen.update()

screen.exitonclick()

# py main.py
