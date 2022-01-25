import turtle
import pandas

IMAGE = "blank_states_img.gif"
FONT = ("Arial", 10, "normal")
ALIGN = "center"

ScreenApp = turtle.Screen()
ScreenApp.addshape(IMAGE)
ScreenApp.title("US State Game")

turtle.shape(IMAGE)
TurtleApp = turtle.Turtle()
TurtleApp.penup()
TurtleApp.hideturtle()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
missed_states = []

while len(guessed_states) < 50:
    user_answer = ScreenApp.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if user_answer == "Exit":
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)
        break

    if user_answer in all_states and user_answer not in guessed_states:
        guessed_states.append(user_answer)
        state_detail = data[data.state == user_answer]
        x_cor = int(state_detail.x)
        y_cor = int(state_detail.y)
        TurtleApp.goto(x_cor, y_cor)
        TurtleApp.write(user_answer, align=ALIGN, font=FONT)

data_dict = {
    "state": missed_states
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("missing_states.csv")