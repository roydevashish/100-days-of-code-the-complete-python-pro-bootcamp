from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LIN_Y = 280

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()  
        self.GoToStart()

    def GoToStart(self):
        self.goto(STARTING_POSITION)

    def GoUp(self):
        self.forward(MOVE_DISTANCE)

    def GoDown(self):
        self.backward(MOVE_DISTANCE)
    
    def IsAtFinishLine(self):
        if self.ycor() > 280:
            return True
        else :
            return False