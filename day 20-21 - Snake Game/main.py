from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with a wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 290 or snake.head.ycor() < -298:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    # list slicing
    # use 1: - to get everything except the first item
    # ### - Tip -  use ::-1 to reverse the list ####
    for turtle in snake.all_turtles[1:]:
        if snake.head.distance(turtle) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
