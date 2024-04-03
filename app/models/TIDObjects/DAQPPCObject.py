# Description: DAQPPCObject model.
from app import db

class DAQPPCObject(db.Model):
    __tablename__ = "DAQPPCObject"
    DAQPPCObjectId = db.Column(db.Integer, primary_key=True)
    projectId = db.Column(db.Integer)
    name = db.Column(db.String(255))
    partNumber = db.Column(db.String(255))

    def json(self):
        return {'id': self.id, 'name': self.name, 'PN': self.PN}
    
    def __init__(self, name, ID, PN):
        self.name = name
        self.DAQPPCObjectId = ID 
        self.partNumber = PN