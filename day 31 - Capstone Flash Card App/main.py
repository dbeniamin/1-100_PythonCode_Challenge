from tkinter import *
import pandas
import random

""" ------- Documentation References -------"""
""" CSV data frame  -> https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html"""
"""change color of the text in a canvas, use the fill parameter. e.g. 
https://stackoverflow.com/questions/41030973/how-can-i-change-the-color-of-text-in-tkinter"""
"""Remember in the mainloop() you should not create additional delayed loops e.g. with time.sleep() but instead, 
use window.after() e.g. Tkinter Reference Manual: .after() method"""
""" Cancel a window.after() loop -> Tkinter Reference Manual: .after_cancel() method """
""" Remove elements from a list -> https://www.w3schools.com/python/ref_list_remove.asp """
""" Create CSV ->  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html """

BACKGROUND_COLOR = "#B1DDC6"
to_learn = []
current_card = {}

# ------------ Read the CSV ------------ #
try:
    data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")


# use orient to separate the data in a list of dicts

# defina global dict as card, so it can be accessed by 2 functions and assigned to separate cards


# ------------ Next Card ------------ #

def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # case-sensitive keys when taping in to a dictionary
    # print(current_card["French"])   -> print statement to check the code
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = canvas.after(3000, func=flip_card)


# ------------ Flip Card ------------ #

def flip_card():
    # title is static as english no matter what word is displayed for english
    # use the fill="" attribute to change the color of the text on the fliped card
    canvas.itemconfig(card_title, text="English", fill="white")
    # acces the current card dict and extract the word for English
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# ------------ Known Card ------------ #

def is_known():
    # when the user chose the green button the curent card is going to be removed from the random generated dict
    to_learn.remove(current_card)
    # print statement to check the code.
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    # setting index=False will no creat index every time the new file is accesed
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ------------ UI configuration ------------ #

window = Tk()
window.title("Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526)
card_background = canvas.create_image(400, 263, image=card_front_img)

# adding text to the canvas created
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))

# set the canvas bg color and elimitate the line with higlightthickness
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# you can add immages to buttons using the below format
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)

# call the function so the labels on canvas will show the language / word randomlly generated
next_card()

window.mainloop()
