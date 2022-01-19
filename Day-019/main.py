import turtle

AppTurtle = turtle.Turtle()
AppScreen = turtle.Screen()

def move_forward():
    AppTurtle.forward(10)

def move_backword():
    AppTurtle.backward(10)

def counter_clockwise():
    AppTurtle.setheading(AppTurtle.heading() + 10)

def clockwise():
    AppTurtle.setheading(AppTurtle.heading() - 10)

def clear():
    AppTurtle.penup()
    AppTurtle.clear()
    AppTurtle.setposition(0, 0)
    AppTurtle.setheading(0)
    AppTurtle.pendown()

AppScreen.listen()

AppScreen.onkey(key="space", fun=move_forward)
AppScreen.onkey(key="w", fun=move_forward)
AppScreen.onkey(key="s", fun=move_backword)
AppScreen.onkey(key="a", fun=counter_clockwise)
AppScreen.onkey(key="d", fun=clockwise)
AppScreen.onkey(key="c", fun=clear)

AppScreen.exitonclick()