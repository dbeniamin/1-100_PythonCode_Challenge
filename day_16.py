from prettytable import PrettyTable
import turtle
from turtle import Screen

### OOP principles ###
### using Turtle for practice purposes ###
### using Prettytable for practice purposes ###

""" practice class attributes and method passing - https://docs.python.org/3/library/turtle.html """
""" practice class and object manipulation - https://pypi.org/project/prettytable/ """

benjamin = turtle.Turtle()

print(benjamin)

my_screen = Screen()
print(my_screen.canvheight)

benjamin.shape("turtle")
benjamin.color("blue1")

benjamin.forward(100)

### method = function tied to an object  ###
my_screen.exitonclick()

# new object
table = PrettyTable()

table.add_column("City", ["Tokyo", "London", "Berlin"])
table.add_column("Move to", ["Yes", "No", "No"])

table.align = "l"

print(table)

