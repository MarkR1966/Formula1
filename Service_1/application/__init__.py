from flask import Flask

app = Flask(__name__)

from randomcharsandnums.Service_1.application import routes