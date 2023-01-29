from flask import Flask

app = Flask(__name__)

def make_bold(function_name):
    def wrapper_function():
        return f"<b>{function_name()}</b>"
    return wrapper_function
    
@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
    "<p>This is a paragraph.</p>" \
    "<img src='https://media.giphy.com/media/3o7TKSjRrfIPjeiVyQ/giphy.gif' alt='gif'>"


@app.route("/what")
@make_bold
def what():
    return "<p>What's up?</p>"



if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)