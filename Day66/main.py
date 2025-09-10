from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return  {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random",methods=["GET"])
def get_random_cafe():
    random_cafe = random.choice(db.session.query(Cafe).all())
    print(random_cafe.name)
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all_cafe")
def all_cafe():
    all_cafe = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafe])

@app.route("/search")
def search():
    user_loc = request.args.get("loc")
    if not user_loc:
        return jsonify(error="pleas provide location"),400
    print(user_loc)
    cafe = db.session.execute(db.select(Cafe).where(Cafe.location.ilike(user_loc))).scalars().all()
    if len(cafe) > 0:
        return jsonify(cafe=[item.to_dict() for item in cafe])
    else:
        return jsonify(error="No cafes found at that location"),404


# HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("has_sockets")),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:id>",methods=["PATCH"])
def update_price(id):
    new_price = request.args.get("new_price")
    try:
        cafe = db.get_or_404(Cafe, id)
    except AttributeError:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}),404
    else:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}),200

# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:id>",methods=["DELETE"])
def delete(id):
    api_key = request.args.get("api-key")
    try:
        cafe = db.get_or_404(Cafe, id)
    except AttributeError:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}),404
    else:
        if api_key=="ILOVEGOD":
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403

if __name__ == '__main__':
    app.run(debug=True)
