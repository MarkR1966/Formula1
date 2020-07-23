from application import app
from flask import render_template

import requests

@app.route('/', methods = ['GET'])
def home():
    response = requests.get('http://service_4:5003').text
    return render_template('home.html', title='Home', display = response)