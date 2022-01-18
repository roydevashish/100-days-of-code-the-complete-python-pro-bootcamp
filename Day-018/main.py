import random
from turtle import Turtle, Screen

AppScreen = Screen()
AppTurtle = Turtle()
AppTurtle.shapesize(0.8, 0.8)
AppTurtle.speed(0)

# Task 1: Draw a square.
def draw_square():
    for _ in range(4):
        AppTurtle.forward(50)
        AppTurtle.left(90)

# draw_square()


# Task 2: To draw a dashed line.
def draw_dashed_line():
    for _ in range(10):
        AppTurtle.pendown()
        AppTurtle.forward(5)
        AppTurtle.penup()
        AppTurtle.forward(5)
        AppTurtle.pendown()

# draw_dashed_line()

# A function that returns a random hex value for color.
def random_color():
    r = lambda: random.randint(0,255)
    return('#%02X%02X%02X' % (r(),r(),r()))

# A function that returns a tuple of random color in RGB formate.
# def random_color():
#     r = random.randrange(0, 256)
#     g = random.randrange(0, 256)
#     b = random.randrange(0, 256)
#     color = (r, g, b)
#     return color

# Task 3: To draw shapes starting from 3 sides to 10 or n sides.
def draw_shapes(sides):
    if sides < 3:
        print("Please give number of sides more than or equal to 3.")
        return False
    for i in range(3, sides+1):
        angle = 360/i
        AppTurtle.color(random_color())
        for _ in range(i):
            AppTurtle.forward(100)
            AppTurtle.right(angle)

# draw_shapes(10)

# Task 4: Make a random walk and for each step choese a random color.
def random_walk():
    AppTurtle.pensize(8)
    AppTurtle.hideturtle()

    canvas_size = min(AppScreen.window_height(), AppScreen.window_width())
    boundary = (canvas_size/2)-50
    direction_list = [0, 90, 180, 270]
    
    while True:
        if AppTurtle.xcor() > boundary:
            AppTurtle.setheading(random.choice([90, 180, 270]))
        elif AppTurtle.xcor() < -boundary:
            AppTurtle.setheading(random.choice([0, 90, 270]))
        elif AppTurtle.ycor() > boundary:
            AppTurtle.setheading(random.choice([0, 180, 270]))
        elif AppTurtle.ycor() < -boundary:
            AppTurtle.setheading(random.choice([0, 90, 180,]))
        else:
            AppTurtle.setheading(random.choice(direction_list))
        
        AppTurtle.color(random_color())
        AppTurtle.forward(30)
        
# random_walk()


# Task 5: Draw Spirograph
def draw_spirograph(gap):
    AppTurtle.pensize(2)

    loop = int(360/gap)

    for _ in range(loop):
        AppTurtle.color(random_color())
        AppTurtle.circle(100)
        AppTurtle.setheading(AppTurtle.heading() + gap)

# draw_spirograph(5)


# Task 6: Hirst Painting
def draw_hirst_painting(dots):
    AppTurtle.penup()
    AppTurtle.hideturtle()
    AppTurtle.setposition(-230, -230)

    color_list = []
    for _ in range(dots):
        color_list.append(random_color())

    for _ in range(dots):
        for _ in range(dots):
            AppTurtle.dot(10, random.choice(color_list))
            AppTurtle.forward(50)

        AppTurtle.setposition(-230, AppTurtle.ycor()+50)

# draw_hirst_painting(10)

AppScreen.exitonclick()