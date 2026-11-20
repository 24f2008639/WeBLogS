from flask import Flask, render_template as rt
app = Flask(__name__)

posts = [
    {
        "author": 'Dhruv Janakala',
        "title": "Evening @Google Mumbai Data Challenge Winner's Ceremony",
        "content": 'Past',
        "date_of_event": 'November 19, 2026',
        "date_of_post": 'November 22, 2026'
    },
    {
        "author": 'Dhruv Janakala',
        "title": "Day @Claude Impact Lab Mumbai",
        "content": 'Upcoming',
        "date_of_event": 'November 21, 2026',
        "date_of_post": 'November 22, 2026'
    }
]

@app.route("/")
def home():
    return rt("home.html", posts=posts)

@app.route("/about")
def about():
    return rt("about.html", title="About")

# localhost is equivalent to 127.0.0.1
if __name__ == "__main__":
    app.run(debug=True)