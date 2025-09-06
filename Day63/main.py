from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String,Float

app = Flask(__name__)

class Base(DeclarativeBase):
    pass
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)

all_books = []

class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title:Mapped[str]=mapped_column(String(100),unique=True,nullable= False)
    author:Mapped[str]= mapped_column(String(100),nullable = False)
    rating: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)


with app.app_context():
    db.create_all()




@app.route('/')
def home():
    data = db.session.query(Books).all()
    return render_template("index.html",all_books=data)


@app.route("/add",methods=["POST","GET"])
def add():
    if request.method=="POST":
        data = request.form.to_dict()
        new_book = Books(title=request.form.get("title"),author=request.form.get("author"),rating=request.form.get("rating"))
        db.session.add(new_book)
        db.session.commit()
        print(request.form.get("title"))
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route("/edit/<int:id>",methods=["POST","GET"])
def edit(id):
    data = db.get_or_404(Books,id)
    print(data.rating)
    if request.method=="POST":
        new_rating = request.form.get("rating")
        print(new_rating)
        data.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html",book = data)
@app.route("/delete/<int:id>", methods=["GET"])
def delete(id):
    book = db.get_or_404(Books,id)
    print(book)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

