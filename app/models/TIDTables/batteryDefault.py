from app import db

class BatteryDefault(db.Model):
    __tablename__ = "BatteryDefault"
    id = db.Column(db.Integer, primary_key=True)
    projectID = db.Column(db.Integer)
    battery = db.Column(db.String(255))
    capacity = db.Column(db.String(255))
    discharge_current = db.Column(db.String(255))

    def json(self):
        return {'id': self.id, 'battery': self.battery, 'capacity': self.capacity, 'discharge_current': self.discharge_current}
    