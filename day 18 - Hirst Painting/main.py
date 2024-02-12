# import colorgram

# ##extract colors from a saved image
# rgb_colors = []
# extracted_colors = colorgram.extract('image.jpg', 30)
#
# for color in extracted_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random

color_list = [(2, 13, 31), (52, 25, 17), (219, 127, 106), (10, 105, 159), (241, 213, 69), (149, 83, 39), (214, 87, 64),
              (164, 162, 32), (157, 7, 24), (156, 63, 102), (11, 63, 32), (97, 6, 19), (206, 74, 104), (11, 96, 57),
              (172, 135, 162), (1, 63, 145), (8, 173, 216), (157, 33, 24), (5, 212, 207), (9, 139, 86), (146, 227, 216),
              (122, 193, 148), (100, 219, 229), (221, 178, 216), (252, 196, 0), (79, 135, 179)]
# 10 spots by 10, spot size 20,  space 50
benjamin = t.Turtle()
benjamin.shape("triangle")
benjamin.color("black")
benjamin.speed("fastest")
benjamin.penup()
benjamin.hideturtle()
t.colormode(255)

benjamin.setheading(220)
benjamin.forward(300)
benjamin.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    benjamin.dot(20, random.choice(color_list))
    benjamin.forward(50)
    if dot_count % 10 == 0:
        benjamin.setheading(90)
        benjamin.forward(50)
        benjamin.setheading(180)
        benjamin.forward(500)
        benjamin.setheading(0)


screen = t.Screen()
screen.exitonclick()







