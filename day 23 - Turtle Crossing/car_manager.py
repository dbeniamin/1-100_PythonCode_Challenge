from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):

        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # used the .hideturtle because one turtle created and stayed in the middle of the screen
        self.hideturtle()
        random_chance = random.randint(1, 6)
        # random car creation based on the random_chance
        # car creation chance becomes 1 in 6 and can be adjusted to fit the desired difficulty
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            # original size is 20 px by 20 px
            # shape stretches by original amount * desired amount
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            # random_y = random.randint(-250, 250)
            new_car.goto(x=300, y=random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            # move it backwards from the starting spawn point-> i.e. from right to left
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += (MOVE_INCREMENT * 0.3)
