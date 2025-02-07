from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_bootstrap import Bootstrap5


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


# set string field for email and keep it visible
# set password field for password and make it invisible
# add validators to not allow the empty fields
class LoginForm(FlaskForm):
    email = StringField(label='Email')
    password = PasswordField(label="Password")
    submit = SubmitField(label="Log in dude !")


app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


# validate on submit and print the email entered
@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
        # print(login_form.email.data)
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
