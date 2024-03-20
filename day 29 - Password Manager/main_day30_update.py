from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = "Calibri"
GREEN = "#005B41"
RED = "#B31312"
GRAY = "#E5CFF7"

""" ------------- Documentation references ------------- """
""" https://tkdocs.com/tutorial/canvas.html - canvas documentation """
""" https://www.w3schools.com/python/python_file_write.asp """
""" messagebox is not a class - hence it requires separate import """
""" import pyperclip to copy the information to the clipboard """
""" json.dump(new_data, data_file, indent=4) -> write file with spacing 4 """
""" json.load() -> read """
""" json.update() -> update the file """


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

    # add the generated lists to make a list available for suffle
    password_list = password_letters + password_numbers + password_symbols
    # shuffle the characters in the final list
    random.shuffle(password_list)

    password = "".join(password_list)
    input_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_entry = input_website.get()
    email_entry = input_username.get()
    pass_entry = input_password.get()
    new_data = {
        website_entry: {
            "email": email_entry,
            "password": pass_entry,
        }
    }
    # use if / else block to check if all fields are filed up and then move forward with the logic
    if len(website_entry) == 0 or len(pass_entry) == 0:
        messagebox.showinfo(title="Error !!", message="Please fill out all the fields !")

    else:
        try:
            # try to open the file
            with open("data.json", "r") as data_file:
                # read the existing data
                data = json.load(data_file)

        except FileNotFoundError:
            # if the file does not exist creeate the file
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # updating old with new data
            data.update(new_data)
            # save updated data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # use .delete(0, END) to clear the entry field
            input_website.delete(0, END)
            input_password.delete(0, END)


# --------------------------- FIND PASS ------------------------------ #
def find_password():
    website = input_website.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No file Found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details saved for {website} you searched")


# ---------------------------- UI SETUP ------------------------------- #

""" adding all the elements required for the UI - buttons, entry fields, labels """
""" input field and buttons need to have the padx / pady passed in the .grid() command """
""" .config(padx= x value , pady= y value) only works for labels """
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, )

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label_website = Label(text="Website :", font=(FONT_NAME, 15, "bold"))
label_website.grid(row=1, column=0)
label_website.config(padx=5, pady=5)

label_username = Label(text="Email/Username", font=(FONT_NAME, 15, "bold"))
label_username.grid(row=2, column=0)
label_username.config(padx=5, pady=5)

label_password = Label(text="Password :", font=(FONT_NAME, 15, "bold"))
label_password.grid(row=3, column=0)
label_password.config(padx=5, pady=5)

input_website = Entry(width=21, font=(FONT_NAME, 15, "bold"))
input_website.grid(row=1, column=1, padx=5, pady=5)
# use .focus() to have the mouse in that specific input field.
input_website.focus()

input_username = Entry(width=40, font=(FONT_NAME, 15, "bold"))
input_username.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
# .insert(index, "string to be pre entered the field") -> index 0 = entry at the begining
input_username.insert(0, "beniamin@email.com")

input_password = Entry(width=21, font=(FONT_NAME, 15, "bold"))
input_password.grid(row=3, column=1, padx=5, pady=5)

button_search = Button(text="Search", width=17, font=(FONT_NAME, 15, "bold"), bg=GRAY, fg=RED, command=find_password)
button_search.grid(row=1, column=2, padx=5, pady=5)

button_generate = Button(text="Generate Password", font=(FONT_NAME, 15, "bold"), bg=GRAY, fg=RED, command=generate_pass)
button_generate.grid(row=3, column=2, padx=5, pady=5)

button_add = Button(text="Add", width=40, font=(FONT_NAME, 15, "bold"), bg=GRAY, fg=GREEN, command=save)
button_add.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

window.mainloop()
