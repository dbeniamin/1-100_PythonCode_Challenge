import turtle
import pandas
import time

### NOTE - The position of the pop-up screen for the input can not be changed ###

screen = turtle.Screen()
screen.title("Romania County Game")
image = "Romania-districts_map.gif"
screen.addshape(image)
turtle.shape(image)
start_time = time.time()


def update_timer():
    elapsed_time = int(time.time() - start_time)
    turtle.clear()  # Clear previous timer display
    turtle.write(f"Time: {elapsed_time}", align="center", font=("Arial", 16, "normal"))
    turtle.ontimer(update_timer, 1000)  # Update every 1000 milliseconds (1 second)


# Start the timer
update_timer()

### getting the location of the click on screen i.e. x and y coordinate
# def get_mouse_location(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_location)
# loop used so the main game window will not close
# turtle.mainloop()

data = pandas.read_csv("counties.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 41:
    # use .title() to be able to verify even if the letters are capitalized
    answer_state = screen.textinput(title=f"{len(guessed_states)}/41 Districts",
                                    prompt="What's the District name ?").title()

    # type exit to end the game
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        # makes a new csv with the missing states for learning purposes
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # checking the user input if it is in the district csv will pull out the row
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
