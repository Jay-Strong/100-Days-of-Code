from snake import Snake
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height= 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()

snake = Snake()

screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move_snake()
   
    

screen.exitonclick()

# py main.py