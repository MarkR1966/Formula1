from application import app
from flask import render_template
from application.models import F1DriversandTeams

import requests

@app.route('/', methods = ['GET'])
def home():
    response = requests.get('http://service_4:5003').text                                           #Get response from Service_4
    #response = "Lewis hamilton and Red Bull"
    #f1dat = F1DriversandTeams.query.order_by(F1DriversandTeams.id)                                             #get records from database to display on web page
    return render_template('home.html', title='Home', pairing = response)#, f1dat = f1dat)            #render webpage showing response
