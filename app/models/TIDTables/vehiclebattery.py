from app import db

class VehicleBattery(db.Model):
    __tablename__ = "VehicleBattery"
    id = db.Column(db.Integer, primary_key=True)
    projectID = db.Column(db.Integer)
    battery = db.Column(db.String(255))
    psv = db.Column(db.String(255))
    ueiv = db.Column(db.String(255))
    batv = db.Column(db.String(255))
    cell = db.Column(db.String(255))
    temp = db.Column(db.String(255))
    loadv = db.Column(db.String(255))
    loadi = db.Column(db.String(255))

    def json(self):
        return {'id': self.id, 'battery': self.battery, 'psv': self.psv, 'ueiv': self.ueiv, 'batv': self.batv, 'cell': self.cell, 'temp': self.temp, 'loadv': self.loadv, 'loadi': self.loadi}