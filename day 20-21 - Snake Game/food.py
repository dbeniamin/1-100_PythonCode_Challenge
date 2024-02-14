from turtle import Turtle
import random


# class created and inherit from super class
# ## --- don't forget to initialize the super class for inheritance purpose --- ##
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

