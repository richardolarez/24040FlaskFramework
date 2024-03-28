from app import db

class flightCompObject(db.Model):
    __tablename__ = "FlightComputer"
    flightCompId = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255))
    partNumber = db.Column(db.String(255))

    def json(self):
        return {'id': self.flightCompId, 'name': self.name, 'PN': self.partNumber}

    def __init__(self, name, ID, partNumber):
        self.name = name
        self.flightCompId = ID 
        self.partNumber = partNumber