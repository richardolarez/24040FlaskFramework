# Desc: PDUObject class to store PDU information
from app import db
class PDUObject(db.Model):
    __tablename__ = "PDUObject"
    pduObjectId = db.Column(db.Integer, primary_key=True)
    projectId = db.Column(db.Integer)
    name = db.Column(db.String(255))
    partNumber = db.Column(db.String(255))


    def json(self):
        return {'id': self.id, 'name': self.name, 'PN': self.PN}
    
    def __init__(self, name, ID, PN):
        self.name = name
        self.pduObjectId = ID 
        self.partNumber = PN