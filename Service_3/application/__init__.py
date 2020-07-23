from flask import Flask

app = Flask(__name__)

from randomcharsandnums.Service_3.application import routes