import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def CreateCar(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            CarApp = Turtle()
            CarApp.shape("square")
            CarApp.shapesize(stretch_len=2, stretch_wid=1)
            CarApp.penup()
            CarApp.color(random.choice(COLORS))
            CarApp.goto(300, random.randint(-250, 250))
            self.all_cars.append(CarApp)

    def MoveCars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        
    def LevelUp(self):
        self.car_speed += MOVE_INCREMENT