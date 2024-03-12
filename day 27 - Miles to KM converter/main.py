from tkinter import *

## NOTE: .config() method is used to modify the configuration options of a widget after it has been created. However,
# the padx and pady options are not directly configurable through the config method for the Entry widget.

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=400, height=200)
# adding a border padding to the working window
window.config(padx=25, pady=25)


# func to calculate the conversion
def button_clicked():
    new_text = format(int(user_input.get()) * 1.609, ".2f")
    label_calculate.config(text=new_text)


# add 3 labels that will not modify
label_1 = Label(text="is equal to ", font=("Arial", 12))
label_1.grid(column=1, row=1)
label_1.config(padx=20, pady=20)

label_2 = Label(text="Miles", font=("Arial", 12))
label_2.grid(column=3, row=0)
label_2.config(padx=20, pady=20)

label_3 = Label(text="KM", font=("Arial", 12))
label_3.grid(column=3, row=1)
label_3.config(padx=20, pady=20)

# add the calculate button and pass the math function
button_calculate = Button(text="Calculate", command=button_clicked)
button_calculate.grid(column=2, row=2)
button_calculate.config(padx=20, pady=20)

# add the entry box
user_input = Entry(width=5, font=("Arial", 20))
# for the entry box the padding should be passed on the .grid() method
user_input.grid(column=2, row=0, padx=20, pady=20)

# calculation results label
label_calculate = Label(text="", font=("Arial", 20))
label_calculate.config(text="0")
label_calculate.grid(column=2, row=1)
label_calculate.config(padx=20, pady=20)

window.mainloop()
