from tkinter import *


# TODO ->  IMPORTANT !!! <- YOU CANT HAVE .grid() AND .pack() IN THE SAME PROGRAM

### Pack ### -> .pack() -> packs all the widget next to each other ina logical format, will start from the top and
# place each widget below the first one. Can use the side="" to spcify where to start with the widgets

### Place ### -> .place() -> precise positioning, provide the X and Y values  x=0 and y=0 will place in the top left
# corner

### Grid ### -> .grid() -> splits the screen in a grid, any number of collumns and rows. .grid(column=0, row=0)
# easy to use when start from 0 and continue for each element to assign new grid positions

### Documentation - http://tcl.tk/man/tcl8.6/TkCmd/entry.htm ###

# Challange 1 - remake the code so the grid has label at 0,0 ; button at 2,2 ; button at 3,0 ; entry at 4,3

def button_clicked():
    print("I got cliked")
    new_text = user_input.get()
    label_practice.config(text=new_text)


window = Tk()
window.title("This is a test Window")
window.minsize(width=600, height=300)
# adding a border padding to the working window, padx = paddig on X axis, pady = padding on Y axis
window.config(padx=10, pady=10)

### Label creation ###
label_practice = Label(text="First Label", font=("Arial", 25, "bold"))
label_practice.config(text="New Text")
label_practice.grid(column=0, row=0)
# adding space or padding on the specific widget
label_practice.config(padx=11, pady=11)

### Button
button_practice = Button(text="Click Me!", command=button_clicked)
button_practice.grid(column=1, row=1)

button_practice_1 = Button(text="Do Not Click Me!", command=button_clicked)
button_practice_1.grid(column=2, row=0)

### Entry
user_input = Entry(width=15)
print(user_input.get())
user_input.grid(column=3, row=2)

# will keep the window active on screen at all times
window.mainloop()
