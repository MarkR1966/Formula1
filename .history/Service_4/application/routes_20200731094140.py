from application import app
from flask import Flask, Response
from application.models import F1DriversandTeams
import requests

@app.route('/', methods = ['GET'])
def generate_driver():
    r_driver = requests.get('http://Service_2:5001/driver').text      #get result from Service_2
    r_team = requests.get('http://Service_3:5002/team').text          #get result from Service_3
    pairing = "Driver " + rdriver + " will drive for " + team        #create response for Service_1
    f1dat = F1DriversandTeams(                                      #create record to persist data in db
            driver=r_driver,
            team=r_team
    )
    db.session.add(f1dat)                                            #add record to database
    db.session.commit()                                             #commit the change to the database
    return Response(pairing, mimetype='text/plain')                 #return response to Service_1 in the correct format
