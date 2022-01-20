from turtle import Screen
from snake import Snake
import time

ScreenApp = Screen()
ScreenApp.setup(width=600, height=600)
ScreenApp.bgcolor("black")
ScreenApp.title("My Snake Game")
ScreenApp.tracer(0)

SnakeApp = Snake()

ScreenApp.listen()
ScreenApp.onkey(SnakeApp.Up, "Up")
ScreenApp.onkey(SnakeApp.Down, "Down")
ScreenApp.onkey(SnakeApp.Left, "Left")
ScreenApp.onkey(SnakeApp.Right, "Right")

is_game_on = True
while is_game_on:
    ScreenApp.update()
    time.sleep(0.1)
    SnakeApp.Move()

ScreenApp.exitonclick()