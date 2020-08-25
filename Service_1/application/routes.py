from application import app, db
from flask import render_template
from application.models import F1dat

import requests

@app.route('/', methods = ['GET'])                                                                  # Define route for home webpage to be displayed
def home():
    response = requests.get('http://service-4:5003').text                                           # Get response from Service_4
    f1dat = F1dat.query.order_by(F1dat.f1id.desc()).limit(5).all()                                  # Get last 5 records in reverse order from database to display on web page
    return render_template('home.html', title='Home', pairing = response, f1dat = f1dat)            # Render webpage showing response from service 4 and records from database
