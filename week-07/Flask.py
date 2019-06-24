from flask import Flask
from flask import render_template
from flask import jsonify
from flask import make_response
from flask import request
import json
import pandas as pd

df = pd.read_csv('dataset.csv')
origin_df = pd.read_csv('Somerset_HP.csv')
property_type = origin_df.property_type.unique()
property_type = origin_df[origin_df.property_type.notna()].property_type.unique()

variables = ['num_bathrooms', 'num_bedrooms', 'num_floors', 'num_recepts', 'outcode']

app = Flask(__name__)

@app.route('/')
def root():
    return 'Hi'

@app.route('/sign')
def information():
    return render_template('collect_information.html', variables = variables, property_type = property_type)


@app.route('/submit_info', methods=["POST"])
def prediction():
    new_house = {
        'outcode': request.form['outcode'],
        'num_bedrooms ': request.form['num_bedrooms'],
        'num_bathrooms': request.form['num_bathrooms'],
        'num_floors': request.form['num_floors'],
        'num_recepts': request.form['num_recepts'],
        'property_type': request.form['property_type']
    }
    response = jsonify(new_house)
    return response

if __name__ == "__main__":
    app.run()
