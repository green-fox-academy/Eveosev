from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
#Try to make a homepage
def index():
    return "Welcomem, this is the html workshop"

@app.route('/<name>')
def exercise(name):
    return render_template(f"{name}.html")

if __name__ == "__main__":
    app.run()