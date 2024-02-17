from app import db

class PowerSupplySummary(db.Model):
    __tablename__ = "PowerSupplySummary"
    id = db.Column(db.Integer, primary_key=True)
    part_number = db.Column(db.String(255))
    voltage = db.Column(db.Float)
    current = db.Column(db.Float)
    power = db.Column(db.Float)

    def json(self):
        return {'id': self.id, 'part_number': self.part_number, 'voltage': self.voltage, 'current': self.current, 'power': self.power}