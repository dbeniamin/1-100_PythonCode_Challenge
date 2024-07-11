from flask import Flask
import random

# randomize the number between 0 and 9
random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


# use https://t.ly/giphy/url-shortener to short the giphy urls
@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9 !! Type /your number in the URL bar</h1>" \
           "<img src='https://t.ly/IoDEd'</img>"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: red'>Too high, try again!</h1>" \
               "<img src='https://t.ly/oP5vM'/img>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://t.ly/GrtbQ'/img>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://t.ly/IzfrU'/img>"


if __name__ == "__main__":
    app.run(debug=True)
