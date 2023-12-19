### reeborg practice - use reeborg.ca for all the practice exercises
### chose Python as a language.

## Loops
## for item in list_of_items:
##     do something to each item

## for number in range(a, b):
##     print(number)

## while something_is_true:
#     do something repeatedly

## making a function

# # defining a function -> def name ()
# def test_function():
#     print("Test")
#     print("Learn")

# # call the function or accessing the function
# test_function()


# def turn_around():
#     turn_left()
#     turn_left()
# move()
# move()
# turn_around()
# move()
# move()
# turn_around()

# # #  EXERCISE NO. 1 - turning draw a square
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# turn_left()
# move()
# move()
# turn_right()
# move()
# move()
# turn_right()
# move()
# move()
# turn_right()
# move()
# move()

# # #  EXERCISE NO. 2 - hurdle 1 - def function
# def robot_jump():
#     move()
#     turn_left()
#     move()
#     turn_left()
#     turn_left()
#     turn_left()
#     move()
#     turn_left()
#     turn_left()
#     turn_left()
#     move()
#     turn_left()

# use the for xxx in range(AA) to repeat the function need for AA times
# for robot in range(6):
#     robot_jump()

# # using while loop to do the same

# number_of_hurdles = 6
# # while number_of_hurdles > 0:
#     robot_jump()
#     number_of_hurdles -= 1

# # #  EXERCISE NO. 3 -  variable position Hurdles 
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()


# # #  EXERCISE NO. 4 - Random height hurdle with random goal
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

# # #  EXERCISE NO. 5 - Reeborg Maze - infinite loop if the right side is empty
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
