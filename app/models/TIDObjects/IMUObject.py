# Description: IMUObject is a class that represents the IMU object in the TID database.
from app import db

class IMUObject(db.Model):
    __tablename__ = "IMUObject"
    IMUObjectId = db.Column(db.Integer, primary_key=True)
    projectId = db.Column(db.Integer)
    name = db.Column(db.String(255))
    partNumber = db.Column(db.String(255))

    def json(self):
        return {'id': self.id, 'name': self.name, 'PN': self.PN}
    
    def __init__(self, name, ID, PN):
        self.name = name
        self.IMUObjectId = ID 
        self.partNumber = PN

