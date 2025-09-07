from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
from dotenv import load_dotenv
import requests


load_dotenv()


MOVIE_URL = "http://www.omdbapi.com"
API_KEY = os.environ.get("MOVIE_API_KEY")


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class Base(DeclarativeBase):
    pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)



class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[Float] = mapped_column(Float, nullable=False, default=0.0)
    ranking: Mapped[Float] = mapped_column(Float, nullable=False)
    review: Mapped[str] = mapped_column(String(100), nullable=False)
    img_url: Mapped[str]


with app.app_context():
    db.create_all()



class UpdateForm(FlaskForm):
    rating = StringField(label="Your rating out of 10", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class Add(FlaskForm):
    title = StringField(label="Movie title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")



def get_movie_by_title(title):
    parameters = {"t": title, "apikey": API_KEY}
    try:
        response = requests.get(MOVIE_URL, params=parameters, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data.get("Response") == "False":
            return None
        return data
    except requests.RequestException:
        return None


def get_movie_by_id(id):
    parameters = {"i": id, "apikey": API_KEY}
    try:
        response = requests.get(MOVIE_URL, params=parameters, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data.get("Response") == "False":
            return None
        return data
    except requests.RequestException:
        return None



@app.route("/")
def home():
    data = db.session.query(Movie).all()
    return render_template("index.html", movies=data)


@app.route("/update/<int:id>", methods=["POST", "GET"])
def update(id):
    form = UpdateForm()
    for_title = db.get_or_404(Movie, id)

    if form.validate_on_submit() and request.method == "POST":
        data = db.get_or_404(Movie, id)
        data.rating = form.rating.data
        data.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", form=form, title=for_title.title)


@app.route("/edit/<id>", methods=["POST", "GET"])
def edit(id):
    movie_data = get_movie_by_id(id)
    if not movie_data:
        flash("Movie details could not be fetched. Please try again.")
        return redirect(url_for("home"))

    form = UpdateForm()
    if form.validate_on_submit() and request.method == "POST":
        rating = form.rating.data
        review = form.review.data
        title = movie_data["Title"]
        year = movie_data["Year"]
        description = movie_data["Plot"]
        poster = movie_data["Poster"]

        new_movie = Movie(
            title=title,
            year=year,
            description=description,
            rating=rating,
            ranking=10,
            review=review,
            img_url=poster
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", form=form, title=movie_data["Title"])


@app.route("/delete/<int:id>", methods=["POST", "GET"])
def delete(id):
    data = db.get_or_404(Movie, id)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["POST", "GET"])
def add():
    form = Add()
    data = db.session.query(Movie).all()
    if request.method == "POST":
        movie_data = get_movie_by_title(form.title.data)
        if not movie_data:
            flash("Movie not found. Please try another title.")
            return redirect(url_for("add"))
        for movie in data:
            if movie.title == movie_data["Title"]:
                flash("Movie already found. Please try another title.")
                return redirect(url_for("add"))
        return render_template("select.html", movies=movie_data)
    return render_template("add.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
