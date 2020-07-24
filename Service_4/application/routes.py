from application import app
from flask import Flask, Response
import requests

@app.route('/', methods = ['GET'])
def generate_driver():
    #driver = requests.get('http://Service_2:5001/driver').text
    #team = requests.get('http://Service_3:5002/team').text
    #pairing = "Driver " + driver + " will drive for " + team
    pairing = "Driver Lewis Hamilton will drive for Red Bull"
    return Response(pairing, mimetype='text/plain')
