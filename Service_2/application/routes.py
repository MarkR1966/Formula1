from application import app
from flask import Flask, Response
import random

@app.route('/driver', methods = ['GET'])
def generate_driver():
    drivers = ("Lewis Hamilton","Max Verstappen","Charles LeClerc","Daniel Ricciardo","Lando Norris","Sergio Perez","Pierre Gasly","Antonio Giovinazzi","Kevin Magnussen","George Russell")
    choose_driver =random.choice(drivers)
    return Response(choose_driver, mimetype='text/plain')
