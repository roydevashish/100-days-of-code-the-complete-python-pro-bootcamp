from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.ReadHighScore()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.UpdateScoreBoard()
        print(self.high_score)
        
    def UpdateScoreBoard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def Reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.WriteHighScore(self.high_score)
        
        self.score = 0
        self.UpdateScoreBoard()
        
    def IncreaseScore(self):
        self.score += 1
        self.UpdateScoreBoard()

    def ReadHighScore(self):
        with open("data.txt") as file:
            high_score = int(file.read())
        
        return high_score
    
    def WriteHighScore(self, high_score):
        with open("data.txt", mode="w") as file:
            file.write(str(high_score))