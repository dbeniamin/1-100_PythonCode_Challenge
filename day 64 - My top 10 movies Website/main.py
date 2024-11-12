from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import requests
import os

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'use_your_own_key'
Bootstrap5(app)

# tmdb setup - urls + personal key
movie_db_url_search = "https://api.themoviedb.org/3/search/movie"
movie_db_key = "get your movie db key"
movie_db_image = "https://image.tmdb.org/t/p/w500"
movie_db_info = "https://api.themoviedb.org/3/movie"
headers_set = {
    "Content-Type": "application/json; charset=utf-8"
}


# data base creeation

class Base(DeclarativeBase):
    pass


# initialize the db
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///the_film_collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# table creation
# make the class
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500))
    rating: Mapped[float] = mapped_column(Float)
    ranking: Mapped[float] = mapped_column(Integer)
    review: Mapped[str] = mapped_column(String(250))
    img_url: Mapped[str] = mapped_column(String(250))


# actually creeate the db with above definede collumn rule
with app.app_context():
    db.create_all()


# # adding items - need to be commented after items are added
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()

class RateMovieForm(FlaskForm):
    rating = StringField(label="Your Rating of the movie", validators=[DataRequired(), ])
    review = StringField(label="Your Review", validators=[DataRequired(), Length(min=1, max=150)])
    submit = SubmitField("Submit")


class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add the Movie")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()  # convert ScalarResult to Python List

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)


# create add route for the new items
@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(movie_db_url_search, params={
            "api_key": movie_db_key, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)


# create find route to find items
@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{movie_db_info}/{movie_api_id}"
        response = requests.get(movie_api_url, params={
            "api_key": movie_db_key, "language": "en-US"
        }, headers=headers_set)
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{movie_db_image}{data['poster_path']}",
            description=data["overview"],
            rating=data.get("rating", 0)
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home", id=new_movie.id))


# edit route for existing items
@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


# delete route to delete existing items
@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
