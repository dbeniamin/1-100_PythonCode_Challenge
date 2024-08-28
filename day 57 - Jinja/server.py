import datetime
import json
import random
import requests

from flask import Flask
from flask import render_template

app = Flask(__name__)


# https://jinja.palletsprojects.com/en/3.1.x/ - documentations for the class

@app.route("/")
def home():
    now = datetime.datetime.now()
    current_year = now.year
    random_num = random.randint(1, 10)
    return render_template("index.html", num=random_num, year=current_year)


@app.route("/guess/<name>")
def auto_update(name):
    # year for the copyright()
    now = datetime.datetime.now()
    current_year = now.year

    name_uppercase = name.capitalize()
    response_age = requests.get(f"https://api.agify.io?name={name}")
    # need to get the text out from the response
    age_text = response_age.text
    # going straight to json returns a TypeError
    age_data = json.loads(age_text)
    age_test = age_data["age"]

    response_gender = requests.get(f"https://api.genderize.io?name={name}")
    gender_text = response_gender.text
    gender_data = json.loads(gender_text)
    gender_test = gender_data["gender"]

    return render_template("index.html", name=name_uppercase, age=age_test, gender=gender_test, year=current_year)


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
