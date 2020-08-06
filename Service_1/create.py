from application import db
from application.models import F1dat

db.drop_all()                           # Drop all tables in the database in case of any structural and relationship changes
db.create_all()                         # create all tables with fields defined in models
