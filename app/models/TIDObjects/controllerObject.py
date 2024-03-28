from app import db

class Controller(db.Model):
    __tablename__ = "Controller"
    controllerId = db.Column(db.String(255), primary_key=True)
    projectId = db.Column(db.Integer)
    name = db.Column(db.String(255))
    partNumber = db.Column(db.String(255))

    def json(self):
        return {'id': self.controllerId, 'name': self.name, 'PN': self.partNumber}

    def __init__(self, name, ID, PN):
        self.name = name
        self.controllerId = str(ID) 
        self.partNumber = PN