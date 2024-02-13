# ### Turtle Race ### #

from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make a BET",
                            "Who will win? Chose a color: red, blue, green, yellow, black, purple")
colors = ["red", "blue", "green", "yellow", "black", "purple"]
y_position = [-100, -65, -30, 5, 40, 75]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 215:
            race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You Won, the Winner is {winner_color}")
            else:
                print(f"You Lost! the Winner color is {winner_color}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
