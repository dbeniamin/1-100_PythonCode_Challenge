# # ### Introduction to Web Development with Flask
import time

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"


# in order to run the code on windows use in the py charm terminal the following commands
# set FLASK_APP=dat_54.py - use your own named file here
# flask --app day_54.py run - use your own named file here

# add bellow lines to run flask direct from pycharm
if __name__ == "__main__":
    app.run()


# Python Decorator

# ### A decorator function is just a function that wraps a function and gives it additional functionality !!!

def test_deco(function):
    def wrapper_func():
        function()

    return wrapper_func


# delay decorator

def delay_deco(function):
    def wrapper_func():
        time.sleep(2)
        # do something before
        function()
        # do something after

    return wrapper_func


# calling the delay decorator to a function using @
@delay_deco
def say_hello():
    print("Hello")


say_hello()


# the funct with not decorator calls instantly
# different way to call the decorator
def say_bye():
    print("Bye")


# name a decorated func -> pass the delay decorator
decorated_func = delay_deco(say_bye)
decorated_func()  # this will run the say_bye using the delay from the main decorator.



