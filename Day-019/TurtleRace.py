import random
from turtle import Turtle, Screen

AppScreen = Screen()
AppScreen.setup(height=400, width=500)

is_race_on = False
user_bet = AppScreen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color (red, orange, yellow, green, blue, purple): ")

color_list = ["purple", "blue", "green", "yellow", "orange", "red"]
turtle_list = []
y_cor = -125
for index in range(6):
    AppTurtle = Turtle(shape="turtle")
    AppTurtle.penup()
    AppTurtle.color(color_list[index])
    AppTurtle.goto(x=-230, y=y_cor)
    y_cor += 50
    turtle_list.append(AppTurtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner.")
            else:
                print(f"You've lost! The {winner} turtle is the winner.")

        random_steps = random.randint(0, 10)
        turtle.forward(random_steps)

AppScreen.exitonclick()