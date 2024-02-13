# ### Etch a Sketch - exercise with turtle ####
from turtle import Turtle, Screen

benji = Turtle()
screen = Screen()


def move_forward():
    benji.forward(10)


def move_backward():
    benji.backward(10)


def turn_left():
    new_heading = benji.heading() + 10
    benji.setheading(new_heading)


def turn_right():
    new_heading = benji.heading() - 10
    benji.setheading(new_heading)


def clear_screen():
    benji.clear()
    benji.penup()
    benji.home()
    benji.pendown()


screen.listen()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()



