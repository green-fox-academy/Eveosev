from flask import Flask
from flask import render_template

app = Flask(__name__)

products = [
    ("Milk", 3.59123),
    ("Bread", 2.96332),
    ("Rice", 0.64111)
]

@app.route('/')
def display_products():
    return render_template('product.html', p = products)

if __name__ == "__main__":
    app.run()