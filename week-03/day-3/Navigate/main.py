from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/movie')
def movie():
    return render_template("movie.html")

@app.route('/movie/<movie_id>')
def LoadMoviePage(movie_id):
    return render_template(f"../static/{movie_id}.html")

if __name__ == "__main__":
    app.run()