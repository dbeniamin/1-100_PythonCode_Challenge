from flask import Flask

app = Flask(__name__)


# create decorators for bold, emphasis and underlined
def make_bold(function):
    def wrapper_func():
        return "<b>" + function + "</b>"

    return wrapper_func


def make_emphasis(function):
    def wrapper_func():
        return "<em>" + function + "</em>"

    return wrapper_func


def make_underlined(function):
    def wrapper_func():
        return "<u>" + function + "</u>"

    return wrapper_func


# any change you made to the function you need to stop and rerun the server
# debug mode on - activates the automatic reloader and enables the debug mode on flask apps
# set debug = True in the app.run params
# can add html tags in the return code
# can add css styling in the return statement


@app.route("/")
def hello_world():
    return ('<h1 style = "text-align: center">Hello World</h1>'
            '<p> "this is a paragraph !!!" </p>'
            '<img src = "https://media4.giphy.com/media/v1'
            '.Y2lkPTc5MGI3NjExaTQzczB3cHV4enN1cG5yc3N3Ymc4bXA4amM2d2tia2M4NXMxNml0aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JoHCsfie23fag/200.webp"</img>')


@app.route("/bye")
# apply previously created decorators.
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name} you are {number} years old"


# http://127.0.0.1:5000/username/<your actual name> the greet() func will apply your name to the message.
# http://127.0.0.1:5000/username/benjamin/39 -> url returns the name and age as int

if __name__ == "__main__":
    app.run(debug=True)


# ## Advanced Decorators

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_deco(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])

    return wrapper


@is_authenticated_deco
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post")


new_user = User("Benjamin")
new_user.is_logged_in = True
create_blog_post(new_user)
