## Tkinter, *args, **kwargs and GUI Programs ###

import tkinter

window = tkinter.Tk()
window.title("This is a test Window")
# use the .minsize() to set a minimum size of the window that appears
# window will scale up in size based on how many elements are in them if size is not provided
window.minsize(width=600, height=300)

### Label creation ###
test_label = tkinter.Label(text="First Label", font=("Arial", 25, "bold"))
# Documentation on the .pack() https://tcl.tk/man/tcl8.6/TkCmd/pack.htm ###

# .pack() print the label and set it in the middle of the screen
test_label.pack(side="left")

# will keep the window active on screen at all times
window.mainloop()


# *args - arguments

## Unlimited positional arguments ###
def add(*args):
    # access the index of the *args tuple
    print(args[0])
    # sum all the *args used to run the function
    sum_of_args = 0
    for n in args:
        sum_of_args += n
    return sum_of_args


print(add(1, 5, 16, 11, 12))


## Unlimited keyword arguments **kwargs  ###
def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)

    # can tap in the kwarg by specifing the key
    print(kwargs["add"])

    print(kwargs["multiply"])

    n += kwargs["add"]
    n *= kwargs["multiply"]


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        # using the .get when definig the function will return None if no arguments are provide
        # not using .get when defining the function will crash the program if no arguments are provided
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("white")


my_car = Car(make="Land Rover", model="Defender")

print(my_car.make, my_car.model)
