import turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    # create the snake
    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = turtle.Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.all_turtles.append(new_turtle)

    def reset(self):
        # for loop to send the lingering segments from the previous snake off the screen
        # in case of game over the segments don't disappear from the screen without sending them to another position
        for seg in self.all_turtles:
            seg.goto(1000, 1000)
        self.all_turtles.clear()
        self.create_snake()
        self.head = self.all_turtles[0]

    def extend(self):
        self.add_segment(self.all_turtles[-1].position())

    # new function in the snake class just for movement
    def move(self):
        for turtle_num in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[turtle_num - 1].xcor()
            new_y = self.all_turtles[turtle_num - 1].ycor()
            self.all_turtles[turtle_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

# define movement functions to control de snake and set heading
# if statements to not let the snake go back on itself
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
