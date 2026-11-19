from flask import Flask
app = Flask(__name__)

@app.route("/")
def greeting():
    return "<h1>Hola Amigos!!<h1>"

# localhost is equivalent to 127.0.0.1
if __name__ == "__main__":
    app.run(debug=True)