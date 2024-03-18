from tkinter import *
import math

""" use https://colorhunt.co/ to get the codes for colors """

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # use the window.after_cancel() to reset the timer variable defined
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer")
    label_check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # use label name.config to change the text and the color of the text
    # for 8th rep
    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Break", fg=RED)

    # for 2nd / 4th / 6th rep
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text="Break", fg=PINK)

    # for 1st / 3rd / 5th / 7th rep
    else:
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)  # returns the largest number without decimals
    count_sec = count % 60  # returns the remaining number afer divided by 60

    # changing the data type based on the content of that variable
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # tap in to .itemconfig() to update the canvas with the timer, passing the item you need to change i.e.
    # timer_text and the thing you want to change for the specific item in form of **kwarg
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        # .after() allows to pass a time indicator in ms, a function and countles positional arguments *args
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        marks = ""
        # make a range from reps and use math.floor to round it down to nearest int
        for _ in range(math.floor(reps / 2)):
            marks += "✓"
        label_check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# create the canvas in order to be able to put an image as a background
# bg=  refers to the background color in hex code or constant previouslly defined
# highlightthickness=0 -> removes the border between the image and the canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# .create_image() needs to pass the location i.e. x = width / 2 and y = height / 2. PhotoImage - allows to read the
# actual image file="the path of the desired file in case you don't have them in the same root"
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 27, "bold"))
canvas.grid(row=1, column=1)

label_timer = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label_timer.grid(row=0, column=1)

button_start = Button(text="Start", font=(FONT_NAME, 15, "bold"), command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", font=(FONT_NAME, 15, "bold"), command=reset_timer)
button_reset.grid(column=2, row=2)

label_check = Label(font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW)
label_check.grid(row=3, column=1)

window.mainloop()
