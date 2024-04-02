from app import db

class DAQDIGITALObject(db.Model):
    __tablename__ = "DAQDigital"
    daqDigitalId = db.Column(db.String(255), primary_key=True)
    projectId = db.Column(db.Integer)
    name = db.Column(db.String(255))
    partNumber = db.Column(db.String(255))

    def json(self):
        return {'id': self.daqDigitalId, 'name': self.name, 'PN': self.partNumber}

    def __init__(self, name, ID, partNumber):
        self.name = name
        self.daqDigitalId = ID 
        self.partNumber = partNumber