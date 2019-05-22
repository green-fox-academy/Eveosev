from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

with open('products.csv', 'r') as p_csv:
    product = p_csv.read().splitlines()

product_dict = {}
product_tags = product[0].split(';')
for row in product[1:]:
    temp = row.split(';')
    product_dict[temp[1]] = [temp[2], temp[3]]

@app.route('/')
def welcomepage():
    return render_template('welcomepage.html')

@app.route('/submit', methods = ['GET','POST'])
def getname():
    if request.method == 'POST':
        name = request.form['name']
    if name in product_dict:
        return f"{name}-- price: {product_dict[name][0]}, qty: {product_dict[name][1]}"
    else:
        return "Do not have this product"

if __name__ == "__main__":
    app.run()
    

