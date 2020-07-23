from application import app
from flask import Flask, Response
import random

@app.route('/team', methods = ['GET'])
def generate_team():
    teams = ("Mercedes","Red Bull","Ferrari","Renault","McLaren")
    choose_team =random.choice(teams)
    return Response(choose_team, mimetype='text/plain')
