from app import db 

class PDUObject(db.Model):
    __tablename__ = "PDU"
    pduId = db.Column(db.String(255), primary_key=True)
    projectId = db.Column(db.Integer)
    name = db.Column(db.String(255))
    partNumber = db.Column(db.String(255))

    def json(self):
        return {'id': self.pduId, 'name': self.name, 'PN': self.partNumber}

    def __init__(self, name, ID, partNumber):
        self.name = name
        self.pduId = ID 
        self.partNumber = partNumber