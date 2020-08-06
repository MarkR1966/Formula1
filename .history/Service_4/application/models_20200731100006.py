from application import db

class F1dat(db.Model):                        # Define Class F1DriversandTeams to hold F1DriverandTeams table data
    f1id = db.Column(db.Integer, primary_key=True)
    driver = db.Column(db.String(30), nullable=False)
    team = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return ''.join(
            [
                'F!datID: ' + str(self.id) + '\n'
                'Driver: ' + self.driver + '\n'
                'Team: ' + self.team + '\n'
            ]
        )
