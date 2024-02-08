### Turtle and GUI ###
### https://docs.python.org/3/library/turtle.html  - documentation for turtle ###

import turtle as t
import random

# from XXXXX import * -> can be used to import everything from a module
# import turtle as t -> assign alias to a long module name to keep it clear in code

benjamin = t.Turtle()
benjamin.shape("triangle")
benjamin.color("black")
benjamin.speed("fastest")
t.colormode(255)

## make a square on the screen ###
for _ in range(4):
    benjamin.forward(100)
    benjamin.right(90)

## draw a dashed line on the screen ###
for _ in range(15):
    benjamin.forward(10)
    benjamin.penup()
    benjamin.forward(10)
    benjamin.pendown()

## draw triangle , square , pentagon, going up to a number of sides with random pen color ### radius = 360 side = 2
draw_colors = ["blue", "cyan", "lawn green", "ivory", "goldenrod", "dark red", "red", "deep pink", "magenta",
               "indigo"]

side = 2
radius = 360


def draw():
    for _ in range(side):
        benjamin.forward(100)
        benjamin.right(radius / side)


for _ in range(8):
    side += 1
    chosen_color = random.choice(draw_colors)
    benjamin.color(chosen_color)

    draw()

##  Random Walk Exercise ###
draw_colors = [
    "yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan",
    "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]


# create function to random generate RGB color code instead of using predefined list


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = (r, g, b)
    return rgb_color


count = 0
while count < 500:

    count += 1
    angles = [0, 90, 180, 270, 360]
    if (-300 < benjamin.xcor() < 300) and (-300 < benjamin.ycor() < 300):
        benjamin.right(random.choice(angles))
        benjamin.pensize(11)
        benjamin.pencolor(random_color())
        benjamin.forward(40)
    else:
        benjamin.right(180)
        benjamin.forward(40)


### Draw a Spirograph - mandala like ###

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = (r, g, b)
    return rgb_color


def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        benjamin.color(random_color())
        benjamin.pensize(4)
        benjamin.circle(150)
        benjamin.setheading(benjamin.heading() + 5)


draw_spirograph(5)  # ## pass the gap size  i.e. the angle offset that is used for each circle.

# exit on click from the turtle screen - keep at the bottom of the file
screen = t.Screen()
screen.exitonclick()
