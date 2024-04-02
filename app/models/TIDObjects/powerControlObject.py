from app import db 

class powerControlObject(db.Model):
    __tablename__ = "PowerControl"
    powerControlId = db.Column(db.String(255), primary_key=True)
    projectId = db.Column(db.Integer)
    name = db.Column(db.String(255))
    partNumber = db.Column(db.String(255))

    def json(self):
        return {'id': self.powerControlId, 'name': self.name, 'PN': self.partNumber}

    def __init__(self, name, ID, partNumber):
        self.name = name
        self.powerControlId = ID 
        self.partNumber = partNumber