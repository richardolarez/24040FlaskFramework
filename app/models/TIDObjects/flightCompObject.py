# This file contains the class definition for the flightCompObject object. This object is used to store the flight company information.
from app import db

class FlightCompObject(db.Model):
    __tablename__ = "FlightCompObject"
    flightCompObjectId = db.Column(db.Integer, primary_key=True)
    projectId = db.Column(db.Integer)
    name = db.Column(db.String(255))
    partNumber = db.Column(db.String(255))

    def json(self):
        return {'id': self.id, 'name': self.name, 'PN': self.PN}
    
    def __init__(self, name, ID, PN):
        self.name = name
        self.flightCompObjectId = ID 
        self.partNumber = PN