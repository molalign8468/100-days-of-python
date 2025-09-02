from flask import Flask, render_template, request
import smtplib
import requests
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_HOST = "smtp.gmail.com"
API_URL = "https://api.npoint.io/f0172adf5f025b0aacfa"

app = Flask(__name__)


def send_email(name, email, phone, message):
    """Send an email with the contact form details."""
    with smtplib.SMTP(SMTP_HOST) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=(
                "Subject: New message\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Phone: {phone}\n"
                f"Message: {message}"
            ),
        )


def fetch_blogs():
    """Fetch blog data from API."""
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, ValueError):
        return []


@app.route("/")
def Home():
    blogs = fetch_blogs()
    return render_template("index.html", blogs=blogs)


@app.route("/about")
def About():
    return render_template("about.html")


@app.route("/post")
def Post():
    return render_template("post.html")


@app.route("/post/<int:post_id>")
def each_post(post_id):
    blogs = fetch_blogs()
    blog = next((b for b in blogs if int(b.get("id", -1)) == post_id), None)
    return render_template("post.html", blog=blog)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone"),
            message=data.get("message"),
        )
        return "<h1>Successfully sent your message</h1>"
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
