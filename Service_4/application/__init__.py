from flask import Flask

app = Flask(__name__)

from randomcharsandnums.Service_4.application import routes