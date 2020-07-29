from application import app
from flask import render_template
from application.models import F1DriversandTeams

import requests

@app.route('/', methods = ['GET'])
def home():
    response = requests.get('http://service_4:5003').text                                           #Get response from Service_4
    f1dat = F1DriversandTeams.select().order_by(-id.desc()).limit(5)                                #select last 5 records from the database to display on screen
    return render_template('home.html', title='Home', pairing = response, f1dat = f1dat)            #render webpage showing response