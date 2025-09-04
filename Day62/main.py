from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired,URL
import pandas as pd
import csv



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    open_time = SelectField(
        'Opening Time e.g. 8AM',
        choices=[("7AM", "7AM"), ("8AM", "8AM"), ("9AM", "9AM"), ("10AM", "10AM")],
        validators=[DataRequired()]
    )
    close_time = SelectField(
        'Closing Time e.g. 5:30PM',
        choices=[("3PM", "3PM"), ("5PM", "5PM"), ("7PM", "7PM")],
        validators=[DataRequired()]
    )
    coffee = SelectField(
        'Coffee Rating',
        choices=[("☕", "☕"), ("☕☕", "☕☕"), ("☕☕☕", "☕☕☕"),
                 ("☕☕☕☕", "☕☕☕☕"), ("☕☕☕☕☕", "☕☕☕☕☕")],
        validators=[DataRequired()]
    )
    wifi = SelectField(
        'WiFi Strength',
        choices=[("✘", "✘"), ("💪", "💪"), ("💪💪", "💪💪"),
                 ("💪💪💪", "💪💪💪"), ("💪💪💪💪", "💪💪💪💪"),
                 ("💪💪💪💪💪", "💪💪💪💪💪")],
        validators=[DataRequired()]
    )
    power = SelectField(
        'Power Availability',
        choices=[("✘", "✘"), ("🔌", "🔌"), ("🔌🔌", "🔌🔌"),
                 ("🔌🔌🔌", "🔌🔌🔌"), ("🔌🔌🔌🔌", "🔌🔌🔌🔌"),
                 ("🔌🔌🔌🔌🔌", "🔌🔌🔌🔌🔌")],
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open_time.data},"
                           f"{form.close_time.data},"
                           f"{form.coffee.data},"
                           f"{form.wifi.data},"
                           f"{form.power.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = list(csv_data)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
