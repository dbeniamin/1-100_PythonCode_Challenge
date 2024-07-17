from flask import Flask
from flask import render_template

app = Flask(__name__)


# Inspect -> Console -> document.body.contentEditable=true
# !!!!!!! Above command to edit all templates straight in the rendered page !!!!

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
