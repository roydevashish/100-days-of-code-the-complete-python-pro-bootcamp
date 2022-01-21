from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.UpdateScoreBoard()
        
    def UpdateScoreBoard(self):
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def GameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        
    def IncreaseScore(self):
        self.score += 1
        self.clear()
        self.UpdateScoreBoard()

