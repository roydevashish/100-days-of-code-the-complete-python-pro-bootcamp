from turtle import Turtle, Screen

app = Turtle()
app.shape("square")
app.color("coral")
app.speed(1)

def makeSquare():
    for _ in range(4):
        app.forward(100)
        app.left(90)

makeSquare()

screen = Screen()
print(screen.canvheight, screen.canvwidth)
screen.exitonclick()