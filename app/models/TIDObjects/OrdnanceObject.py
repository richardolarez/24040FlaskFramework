from app import db

class OrdnanceObject(db.Model):
    __tablename__ = "Ordnance"
    ordnanceId = db.Column(db.String(255), primary_key=True)
    projectId = db.Column(db.Integer)
    name = db.Column(db.String(255))
    partNumber = db.Column(db.String(255))

    def json(self):
        return {'id': self.ordnanceId, 'name': self.name, 'PN': self.partNumber}

    def __init__(self, name, ID, partNumber):
        self.name = name
        self.ordnanceId = ID 
        self.partNumber = partNumber