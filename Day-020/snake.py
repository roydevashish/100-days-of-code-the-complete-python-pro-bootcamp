from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.turtles = []
        self.CreateSnake()
        self.head = self.turtles[0]

    def CreateSnake(self):
        for position in STARTING_POSITIONS:
            TurtleApp = Turtle("square")
            TurtleApp.color("white")
            TurtleApp.penup()
            TurtleApp.goto(position)    
            self.turtles.append(TurtleApp)

    def Move(self):
        for i in range(len(self.turtles)-1, 0, -1):
            newx = self.turtles[i-1].xcor()
            newy = self.turtles[i-1].ycor()
            self.turtles[i].goto(newx, newy)
        self.head.forward(MOVE_DISTANCE)

    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT) 