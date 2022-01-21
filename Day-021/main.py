from turtle import Screen
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
import time

ScreenApp = Screen()
ScreenApp.setup(width=600, height=600)
ScreenApp.bgcolor("black")
ScreenApp.title("My Snake Game")
ScreenApp.tracer(0)

SnakeApp = Snake()
FoodApp = Food()
ScoreBoardApp = ScoreBoard() 

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

    if SnakeApp.head.distance(FoodApp) < 15:
        FoodApp.Refresh()
        SnakeApp.Extend()
        ScoreBoardApp.IncreaseScore()

    if SnakeApp.head.xcor() > 280 or SnakeApp.head.xcor() < -280 or SnakeApp.head.ycor() > 280 or SnakeApp.head.ycor() < -280:
        ScoreBoardApp.GameOver()
        is_game_on = False

    for each in SnakeApp.turtles[1:]:
        if SnakeApp.head.distance(each) < 10:
            is_game_on = False
            ScoreBoardApp.GameOver()

ScreenApp.exitonclick()