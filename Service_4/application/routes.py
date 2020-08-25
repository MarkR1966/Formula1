from application import app, db
from flask import Flask, Response
from application.models import F1dat
import requests

@app.route('/', methods = ['GET'])
def generate_driver():
    r_driver = requests.get('http://service-2:5001/driver').text        # Get result from Service_2
    r_team = requests.get('http://service-3:5002/team').text            # Get result from Service_3
    pairing = "Driver " + r_driver + " will drive for " + r_team        # Create response for Service_1
    f1dat = F1dat(                                                      # Create record to persist data in db
            driver=str(r_driver),
            team=str(r_team)
    )
    db.session.add(f1dat)                                               # Add record to database
    db.session.commit()                                                 # Commit the change to the database
    return Response(pairing, mimetype='text/plain')                     # Return response to Service_1 in the correct format
