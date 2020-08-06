from application import app
from flask import Flask, Response
import random

@app.route('/team', methods = ['GET'])
def generate_team():                                                                        # Generate random team for Service_4
    teams = ("Mercedes","Red Bull","Ferrari","Renault","McLaren","Racing Point","AlphaTauri","Alfa Romeo Racing","Haas F1 Team","Williams")     # Generate list of teams
    choose_team =random.choice(teams)                                                       # Select random team from the list
    return Response(choose_team, mimetype='text/plain')                                     # Return team to Service_4
