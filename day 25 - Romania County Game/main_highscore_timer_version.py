import turtle
import pandas
import time

screen = turtle.Screen()
screen.title("Romania County Game")
image = "Romania-districts_map.gif"
screen.addshape(image)
turtle.shape(image)

# make a turtle for the timer
timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()

# make a turtle for the high score
high_score_turtle = turtle.Turtle()
high_score_turtle.hideturtle()
high_score_turtle.penup()

# make a turtle for writing districts
district_turtle = turtle.Turtle()
district_turtle.hideturtle()
district_turtle.penup()
district_turtle.color("blue")
# fontsize - might give you a spell check warning. you need to ignore it
district_turtle.fontsize = 15

start_time = time.time()
# make a condition to determine when game ends
game_active = True
guessed_states = []

# read the high score from the text file
with open("lowest_times.txt", "r") as file:
    times = [line.strip() for line in file.readlines()]

# get the high score time
if times:
    lowest_time = min(times)
    high_score_turtle.goto(50, screen.window_height() / 2 - 30)
    high_score_turtle.write(f"High Score: {lowest_time}", align="right", font=("Arial", 16, "normal"))


def update_timer():
    if not game_active:
        return

    time_passed = int(time.time() - start_time)
    minutes_passed = time_passed // 60
    seconds_passed = time_passed % 60

    # use the :02d in a f"" string to show only 2 digits based on the division
    time_format = f"{int(minutes_passed)}:{seconds_passed:02d}"
    timer_turtle.clear()
    timer_turtle.goto(screen.window_width() / 2 - 30, screen.window_height() / 2 - 30)
    timer_turtle.write(f"Time: {time_format}", align="right", font=("Arial", 16, "normal"))
    # timer update every 1000 milliseconds -> 1 second
    screen.ontimer(update_timer, 1000)  # Update every 1000 milliseconds (1 second)


# start the timer
update_timer()

data = pandas.read_csv("counties.csv")
all_states = data.state.to_list()

while len(guessed_states) < 41:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/41 Districts",
                                    prompt="What's the District name ?").title()

    if answer_state == "Exit":
        # stop the game
        game_active = False
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        x_coord, y_coord = int(state_data.x), int(state_data.y)
        district_turtle.goto(x_coord, y_coord)
        district_turtle.write(answer_state, align="center", font=("Arial", district_turtle.fontsize, "normal"))

# stop the time when the game ends
# this mean all 41 guessed states or user types exit in the promp bar
end_time = time.time()
elapsed_time = end_time - start_time
minutes = int(elapsed_time // 60)
seconds = int(elapsed_time % 60)
formatted_time = f"{minutes}:{seconds:02d}"

# save the time in the txt file if all states are guessed
if len(guessed_states) == 41:
    with open("lowest_times.txt", "a") as file:
        file.write(formatted_time + "\n")

# show the final game time
timer_turtle.clear()
timer_turtle.goto(screen.window_width() / 2 - 30, screen.window_height() / 2 - 30)
timer_turtle.write(f"Final Time: {formatted_time}", align="right", font=("Arial", 16, "normal"))

turtle.mainloop()
