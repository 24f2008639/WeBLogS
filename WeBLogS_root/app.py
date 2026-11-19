from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hola Amigos!!<h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

# localhost is equivalent to 127.0.0.1
if __name__ == "__main__":
    app.run(debug=True)