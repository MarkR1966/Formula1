from application import app
from flask import render_template

import requests

@app.route('/', methods = ['GET'])
def home():
    #response = requests.get('http://service_4:5003').text
    responce = "Driver Lewis Hamilton will drive for Renault"
    return render_template('home.html', title='Home', pairing = response)