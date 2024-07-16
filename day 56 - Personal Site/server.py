from flask import Flask
from flask import render_template

app = Flask(__name__)


# https://flask.palletsprojects.com/en/3.0.x/quickstart/#
# use the flask documentation to help navigate the tasks
# static folder - photos and css file
# templates folder - html file

# hard reload = shift + reload button


# Inspect -> Console -> document.body.contentEditable=true
# !!!!!!! Above command to edit all templates straight in the rendered page !!!!

@app.route("/")
def home():
    return render_template("index_1.html")


if __name__ == "__main__":
    app.run(debug=True)
