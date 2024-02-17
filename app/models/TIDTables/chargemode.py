from app import db

class ChargeMode(db.Model):
    __tablename__ = "ChargeMode"
    id = db.Column(db.Integer, primary_key=True)
    battery = db.Column(db.String(255))
    voltage_setting = db.Column(db.Float)
    ovp = db.Column(db.Float)
    current_setting = db.Column(db.Float)
    current_limit = db.Column(db.Float)
    red_green_limits = db.Column(db.String(255))

    def json(self):
        return {'id': self.id, 'battery': self.battery, 'voltage_setting': self.voltage_setting, 'ovp': self.ovp, 'current_setting': self.current_setting, 'current_limit': self.current_limit, 'red_green_limits': self.red_green_limits}