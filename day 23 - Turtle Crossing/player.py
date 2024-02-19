from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.reset_position()
        self.setheading(90)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.penup()
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def finish_reached(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
