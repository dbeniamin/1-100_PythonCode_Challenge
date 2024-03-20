from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT_NAME = "Calibri"
GREEN = "#008170"
BLUE = "#0766AD"
RED = "#B31312"
GRAY = "#E5CFF7"

""" ------------- Documentation references ------------- """
""" https://tkdocs.com/tutorial/canvas.html - canvas documentation """
""" https://www.w3schools.com/python/python_file_write.asp """
""" messagebox is not a class - hence it requires separate import """
""" import pyperclip to copy the information to the clipboard """


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    # delete the pass every time you press the generate button
    input_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(4, 8)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # use list comprehension to loop the available options in the lists the random generated number by saved variables
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    # shuffle the characters in the final list
    random.shuffle(password_list)

    password = "".join(password_list)
    input_password.insert(0, password)
    # copy the pass to clipboard
    pyperclip.copy(password)


# ---------------------------- SHOW PASSWORD ------------------------------- #
def show_password():
    website_entry = input_website.get().lower()
    data_file = open("data.txt", "r")
    for line in data_file:
        stored_website, _, stored_password = line.strip().lower().split(" | ")
        if website_entry == stored_website:
            input_password.delete(0, END)
            input_password.insert(0, stored_password)
            break
    else:
        messagebox.showinfo(title=website_entry, message=f"No password found for {website_entry}")
    data_file.close()


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_entry = input_website.get().lower()
    email_entry = input_username.get()
    pass_entry = input_password.get()
    # use if / else block to check if all fields are filed up and then move forward with the logic
    if len(website_entry) == 0 or len(pass_entry) == 0:
        messagebox.showinfo(title="Error !!", message="Please fill out all the fields !")
    else:
        data_file = open("data.txt", "r")
        lines = data_file.readlines()
        data_file.close()

        modified_lines = []

        for line in lines:
            stored_website, _, _ = line.strip().lower().split(" | ")
            if website_entry == stored_website:
                # search if the website is already saved then ->  update the password
                line = f"{website_entry} | {email_entry} | {pass_entry}\n"
                input_password.delete(0, END)
                input_password.insert(0, pass_entry)
            modified_lines.append(line)

        data_file = open("data.txt", "w")
        data_file.writelines(modified_lines)
        data_file.close()

        if website_entry not in [stored_website for stored_website, _, _ in
                                 (line.strip().lower().split(" | ") for line in lines)]:
            # search if the website is not found then -> add a new line
            data_file = open("data.txt", "a")
            data_file.write(f"{website_entry} | {email_entry} | {pass_entry}\n")

        # clear the website and pasword field when you press add
        input_website.delete(0, END)
        input_password.delete(0, END)

        # close the file
        data_file.close()


# ---------------------------- UI SETUP ------------------------------- #

""" adding all the elements required for the UI - buttons, entry fields, labels """
""" input field and buttons need to have the padx / pady passed in the .grid() command """
""" .config(padx= x value , pady= y value) only works for labels """

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label_website = Label(text="Website :", font=(FONT_NAME, 15, "bold"))
label_website.grid(row=1, column=0)
label_website.config(padx=5, pady=5)

label_username = Label(text="Email/Username :", font=(FONT_NAME, 15, "bold"))
label_username.grid(row=2, column=0)
label_username.config(padx=5, pady=5)

label_password = Label(text="Password :", font=(FONT_NAME, 15, "bold"))
label_password.grid(row=3, column=0)
label_password.config(padx=5, pady=5)

input_website = Entry(width=40, font=(FONT_NAME, 15, "bold"))
input_website.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
# use .focus() to have the mouse in that specific input field.
input_website.focus()

input_username = Entry(width=40, font=(FONT_NAME, 15, "bold"))
input_username.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
# .insert(index, "string to be pre entered the field") -> index 0 = entry at the begining
input_username.insert(0, "beniamin@email.com")

input_password = Entry(width=21, font=(FONT_NAME, 15, "bold"))
input_password.grid(row=3, column=1, padx=5, pady=5)

button_generate = Button(text="Generate Password", font=(FONT_NAME, 15, "bold"), bg=GRAY, fg=BLUE, command=generate_pass)
button_generate.grid(row=3, column=2, padx=5, pady=5)

button_add = Button(text="Add", width=40, font=(FONT_NAME, 15, "bold"), bg=GRAY, fg=GREEN, command=save)
button_add.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

button_show_password = Button(text="Show Password", width=40, font=(FONT_NAME, 15, "bold"), bg=GRAY, fg=RED,
                              command=show_password)
button_show_password.grid(row=5, column=1, columnspan=2, padx=5, pady=5)

window.mainloop()
