from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/939eb0ecdd4b45d4f0ef"
response = requests.get(blog_url)
all_posts = response.json()

@app.route("/")
def home():
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
    requested_post = all_posts[index - 1]
    print(requested_post)
    return render_template("post.html", post=requested_post, image=requested_post['image_url'])
    

if __name__ == "__main__":
    app.run(debug=True)


