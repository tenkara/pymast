from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    blog_url = "https://api.npoint.io/939eb0ecdd4b45d4f0ef"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def post(index):
    requested_post = None
    blog_url = "https://api.npoint.io/939eb0ecdd4b45d4f0ef"
    response = requests.get(blog_url)
    all_posts = response.json()
    for post in all_posts:
        if post["id"] == index:
            requested_post = post
            return render_template("post.html", post=requested_post)
    

if __name__ == "__main__":
    app.run(debug=True)


