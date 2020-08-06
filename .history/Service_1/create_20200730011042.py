from application import db
from application.models import F1DriversandTeams

db.drop_all()
db.create_all()
