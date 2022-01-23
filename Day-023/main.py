import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

ScreenApp = Screen()
ScreenApp.setup(width=600, height=600)
ScreenApp.tracer(0)

PlayerApp = Player()
CarManagerApp = CarManager()
ScoreBoardApp = ScoreBoard()

ScreenApp.listen()
ScreenApp.onkey(PlayerApp.GoUp, "Up")
ScreenApp.onkey(PlayerApp.GoDown, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ScreenApp.update()
    CarManagerApp.CreateCar()
    CarManagerApp.MoveCars()

    # detect collison with car
    for car in CarManagerApp.all_cars:
        if car.distance(PlayerApp) < 20:
            game_is_on = False
            ScoreBoardApp.GameOver()

    # detect sucessfull cor
    if PlayerApp.IsAtFinishLine():
        PlayerApp.GoToStart()
        CarManagerApp.LevelUp()
        ScoreBoardApp.IncreaseLevel()

ScreenApp.exitonclick()