from flask import Flask, render_template as rt
app = Flask(__name__)

@app.route("/")
def home():
    return rt("home.html")

@app.route("/about")
def about():
    return rt("about.html")

# localhost is equivalent to 127.0.0.1
if __name__ == "__main__":
    app.run(debug=True)