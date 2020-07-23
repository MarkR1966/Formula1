from flask import Flask

app = Flask(__name__)

from randomcharsandnums.Service_2.application import routes