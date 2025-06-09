from turtle import Screen
import scoreboard
import paddle
import ball
from pong_court import Court
import time
from random import randint

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
    game_ball.move()

    # Detect collision with wall
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.wall_bounce()
    
     # Detect collision paddles
    if game_ball.distance(right_paddle) < 50 and game_ball.xcor() > 330 or game_ball.distance(left_paddle) < 50 and game_ball.xcor() < -330:
        game_ball.paddle_bounce()

    # Keeping Score
    if game_ball.xcor() >= 400:
        left_score.add_point()
        game_ball.home()
    elif game_ball.xcor() <= -400:
        right_score.add_point()
        game_ball.home()

screen.exitonclick()

# py main.py
