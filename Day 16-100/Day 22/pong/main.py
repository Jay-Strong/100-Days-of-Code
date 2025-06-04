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

    if not ball.is_right:
        ball.serve_left()
    elif not ball.is_left:
        ball.serve_right()
    else:
        ball.start_game()

    if ball.xcor() > 390:
        right_score.score += 1
        left_score.refresh()
        ball.home()
    elif ball.xcor() < -390:
        left_score.score =+ 1
        right_score.refresh()
        ball.home()
    
    screen.update()

screen.exitonclick()

# py main.py
