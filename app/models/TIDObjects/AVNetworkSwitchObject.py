from app import db

class AVNetworkSwitchObject(db.Model):
    __tablename__ = "AVNetworkSwitchObject"
    avnId = db.Column(db.String(255), primary_key=True)
    projectID = db.Column(db.Integer)
    name = db.Column(db.String(255))
    partNumber = db.Column(db.String(255))

    def json(self):
        return {'id': self.avnId, 'name': self.name, 'PN': self.partNumber}

    def __init__(self, name, Id, partNumber):
        self.name = name
        self.avnId = str(Id)
        self.partNumber = partNumber