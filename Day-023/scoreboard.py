from turtle import Turtle
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.level = 1
        self.UpdateScoreBoard()

    def UpdateScoreBoard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def IncreaseLevel(self):
        self.level += 1
        self.UpdateScoreBoard()

    def GameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font= FONT)