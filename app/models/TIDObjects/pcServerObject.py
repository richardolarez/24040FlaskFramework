# Desc: PC Server Object
from app import db

class PCServerObject(db.Model):
    __tablename__ = "PCServerObject"
    pcServerObjectId = db.Column(db.Integer, primary_key=True)
    projectId = db.Column(db.Integer)
    name = db.Column(db.String(255))
    partNumber = db.Column(db.String(255))

    def json(self):
        return {'id': self.id, 'name': self.name, 'PN': self.PN}
    
    def __init__(self, name, ID, PN):
        self.name = name
        self.pcServerObjectId = ID 
        self.partNumber = PN

