from app import db

class VehicleBattery(db.Model):
    __tablename__ = "VehicleBattery"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    capacity = db.Column(db.Float)
    pn = db.Column(db.String(255))
    description2 = db.Column(db.String(255))
    capacity2 = db.Column(db.Float)
    pn2 = db.Column(db.String(255))

    def json(self):
        return {'id': self.id, 'description': self.description, 'capacity': self.capacity, 'pn': self.pn, 'description2': self.description2, 'capacity2': self.capacity2, 'pn2': self.pn2}