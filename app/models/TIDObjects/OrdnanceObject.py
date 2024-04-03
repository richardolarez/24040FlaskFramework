# Description: OrdnanceObject class
# The OrdnanceObject class is a class that represents the Ordnance object in the TID.
from app import db

class OrdnanceObject:
    __tablename__ = "OrdnanceObject"
    OrdnanceObjectId = db.Column(db.Integer, primary_key=True)
    projectId = db.Column(db.Integer)
    name = db.Column(db.String(255))
    partNumber = db.Column(db.String(255))

    def json(self):
        return {'id': self.id, 'name': self.name, 'PN': self.PN}
    
    def __init__(self, name, ID, PN):
        self.name = name
        self.OrdnanceObjectId = ID 
        self.partNumber = PN