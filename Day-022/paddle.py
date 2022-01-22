from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(x_cor, 0)

    def GoUp(self):
        y_cor = self.ycor() + 20
        self.goto(self.xcor(), y_cor)

    def GoDown(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)    