from flask import Flask, render_template, abort
import requests

app = Flask(__name__)

API_URL = "https://api.npoint.io/c790b4d5cab58020d391"

def fetch_blogs():
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()  
        return response.json()
    except (requests.RequestException, ValueError):
        return [] 

@app.route("/")
def home():
    blogs = fetch_blogs()
    return render_template("index.html", blogs=blogs)

@app.route("/post/<int:post_id>")
def each_post(post_id):
    blogs = fetch_blogs()
    blog = next((b for b in blogs if int(b["id"]) == post_id), None)
    if blog is None:
        abort(404) 
    return render_template("post.html", blog=blog)

if __name__ == "__main__":
    app.run(debug=True)
