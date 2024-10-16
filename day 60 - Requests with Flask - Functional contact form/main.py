from flask import Flask, render_template, request
import smtplib
import requests

posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()
# please use your own email and password to make it work
# NOTE - use venv to store them, so it won't be hardcoded
OWN_EMAIL = "test@gmail.com"
OWN_PASSWORD = "practice_test_pass"
app = Flask(__name__)


@app.route('/')
def get_all_posts():
    # all_posts = posts -> as parameter for return render_template required if the blog has multiple
    return render_template("index.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


# contact route to redirect to contact form
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


# send mail func using smtplib module - adding mandatory arguments
def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)
