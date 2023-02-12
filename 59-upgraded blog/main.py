from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)

blog_url = "https://api.npoint.io/939eb0ecdd4b45d4f0ef"
response = requests.get(blog_url)
all_posts = response.json()
EMAIL_ADDRESS = "your email"
EMAIL_PASSWORD = "your password"

@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

@app.route("/post/<int:index>")
def post(index):
    requested_post = all_posts[index - 1]
    print(requested_post)
    return render_template("post.html", post=requested_post, image=requested_post['image_url'])
    
def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        connection.sendmail(EMAIL_ADDRESS,  EMAIL_ADDRESS, email_message)

if __name__ == "__main__":
    app.run(debug=True)


