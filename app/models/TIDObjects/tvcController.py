from app import db 

class TVCCtrl(db.Model):
    __tablename__ = "TVCController"
    tvcId = db.Column(db.String(255), primary_key=True)
    projectId = db.Column(db.Integer)
    name = db.Column(db.String(255))
    partNumber = db.Column(db.String(255))

    def json(self):
        return {'id': self.tvcId, 'name': self.name, 'PN': self.partNumber}

    def __init__(self, name, ID, partNumber):
        self.name = name
        self.tvcId = ID 
        self.partNumber = partNumber