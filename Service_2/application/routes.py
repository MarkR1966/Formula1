from application import app
from flask import Flask, Response
import random

@app.route('/driver', methods = ['GET'])                                                            
def generate_driver():                                                      # Generate random driver for Service_4
    drivers = ("Lewis Hamilton","Max Verstappen","Charles LeClerc","Daniel Ricciardo","Lando Norris","Sergio Perez","Pierre Gasly",
    "Antonio Giovinazzi","Kevin Magnussen","George Russell")                # Define list of Drivers names to select
    choose_driver =random.choice(drivers)                                   # Select random name from the list
    return Response(choose_driver, mimetype='text/plain')                   # Return the Driver to Service_4
