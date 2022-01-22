import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

ScreenApp = Screen()
ScreenApp.bgcolor("black")
ScreenApp.setup(width=800, height=600)
ScreenApp.title("PONG")
ScreenApp.tracer(0)

ScoreBoardApp = ScoreBoard()
BallApp = Ball()
LeftPaddle = Paddle(-350)
RightPaddle = Paddle(350)

# def GoUp():
#     y_cor = PaddleApp.ycor() + 20
#     PaddleApp.goto(PaddleApp.xcor(), y_cor)

# def GoDown():
#     y_cor = PaddleApp.ycor() - 20
#     PaddleApp.goto(PaddleApp.xcor(), y_cor)

ScreenApp.listen()
ScreenApp.onkey(RightPaddle.GoUp, "Up")
ScreenApp.onkey(RightPaddle.GoDown, "Down")

ScreenApp.onkey(LeftPaddle.GoUp, "w")
ScreenApp.onkey(LeftPaddle.GoDown, "s")

game_is_on = True
while game_is_on:
    time.sleep(BallApp.ball_speed)
    ScreenApp.update()
    BallApp.Move()

    # collision with vertical wall
    if BallApp.ycor() > 280 or BallApp.ycor() < -280:
        BallApp.BounceY()

    # collison with the paddles
    if (BallApp.distance(RightPaddle) < 50 and BallApp.xcor() > 320) or (BallApp.distance(LeftPaddle) < 50 and BallApp.xcor() > -320):
        BallApp.BounceX()

    # collision with horizontal wall (posotive x)
    if BallApp.xcor() > 380:
        BallApp.ResetPosition()
        ScoreBoardApp.LeftScore()

    # collision with horizontal wall (negative x)
    if BallApp.xcor() < -380: 
        BallApp.ResetPosition()
        ScoreBoardApp.RightScore()

ScreenApp.exitonclick()