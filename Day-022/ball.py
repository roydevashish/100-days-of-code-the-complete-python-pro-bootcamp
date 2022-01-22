from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = 10
        self.y = 10
        self.ball_speed = 0.1

    def Move(self):
        x_cor = self.xcor() + self.x
        y_cor = self.ycor() + self.y
        self.goto(x_cor, y_cor)

    def BounceY(self):
        self.y *= -1
    
    def BounceX(self):
        self.x *= -1
        self.ball_speed *= 0.9
        
    def ResetPosition(self):
        self.x *= -1
        self.ball_speed = 0.1