from application import db

class F1dat(db.Model):                                          # Define Class F1dat to hold f1dat table data
    f1id = db.Column(db.Integer, primary_key=True)              # Define f1id field as primary key
    driver = db.Column(db.String(30), nullable=False)           # Define driver field as string length 30 cant be NULL 
    team = db.Column(db.String(30), nullable=False)             # Define team field as string length 30 cant be NULL

    def __repr__(self):
        return ''.join(
            [
                'F1ID: ' + str(self.f1id) + '\n'
                'Driver: ' + self.driver + '\n'
                'Team: ' + self.team + '\n'
            ]
        )
