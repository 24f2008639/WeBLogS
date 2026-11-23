from flask import Flask, render_template as rt, url_for
from datetime import datetime

app = Flask(__name__)

blogs_data = [
    {
        "author": 'Dhruv Janakala',
        "title": "Evening @Google Mumbai Data Challenge Winner's Ceremony",
        "content": 'Past',
        "content_file": 'blog-0000000000001.html',
        "date_of_event": 'November 19, 2026',
        "date_of_post": 'November 23, 2026'
    },
    {
        "author": 'Dhruv Janakala',
        "title": "Day @Claude Impact Lab Mumbai",
        "content": 'Past',
        "content_file": 'blog-0000000000002.html',
        "date_of_event": 'November 21, 2026',
        "date_of_post": 'November 23, 2026'
    }
]

def post_date(blog):
    return datetime.strptime(blog["date_of_post"], "%B %d, %Y")

@app.route("/")
@app.route("/home")
def home():
    global blogs
    blogs = sorted(blogs_data, key=post_date, reverse=True)
    return rt("home.html", posts=blogs)

@app.route("/article/<filename>")
def article(filename):
    if filename not in [p["content_file"] for p in blogs]:
        abort(404)
    return rt("article/" + filename)

@app.route("/about")
def about():
    return rt("about.html", title="About")

# localhost is equivalent to 127.0.0.1
if __name__ == "__main__":
    app.run(debug=True)