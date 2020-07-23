from flask import Flask, Response
import requests

@app.route('/', methods = ['GET'])
def generate_driver():
    driver = requests.get('http://Service_2:5001/driver').text
    team = requests.get('http://Service_2:5002/team').text
    display = "Driver " + driver + " will drive for " + team
    return Response(display, mimetype='text/plain')
