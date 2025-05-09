from turtle import Screen, Turtle
import time


screen = Screen()
screen.setup(width=600, height= 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")
segments = []


for num in range(3):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto((-20 * num), 0)
    segments.append(new_segment)


def turn_left() -> None:
    segments[0].left(90)


def turn_right() -> None:
    segments[0].right(90)



def move_snake() -> None:
    screen.listen()
    screen.onkey(fun=turn_left, key="Left")
    screen.onkey(fun=turn_right, key="Right")
    
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    
    
    
    # segments[2].goto(segments[1].position())
    # segments[1].goto(segments[0].position())
    # segments[0].forward(20)




screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)
    move_snake()
   
    

screen.exitonclick()

# py main.py