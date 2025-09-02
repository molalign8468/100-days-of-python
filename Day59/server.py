from flask import Flask,render_template
import requests
app = Flask(__name__)

API_URL = "https://api.npoint.io/f0172adf5f025b0aacfa"

def fetch_blogs():
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()  
        return response.json()
    except (requests.RequestException, ValueError):
        return [] 



@app.route("/")
def Home():
    blogs = fetch_blogs()
    return render_template("index.html",blogs=blogs)

@app.route("/About")
def About():
    return render_template("about.html")

@app.route("/post")
def Post():
    return render_template("post.html")
@app.route("/contact")
def Contact():
    return render_template("contact.html")

@app.route("/post/<int:id>")
def each_post(id):
    blogs = fetch_blogs()
    blog = next((b for b in blogs if int(b["id"]) == id), None)
    return render_template("post.html",blog = blog)

if __name__ == "__main__":
    app.run(debug=True)