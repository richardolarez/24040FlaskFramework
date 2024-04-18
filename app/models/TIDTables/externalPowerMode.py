from app import db

class ExternalMode(db.Model):
    __tablename__ = "ExternalMode"
    id = db.Column(db.Integer, primary_key=True)
    projectID = db.Column(db.Integer)
    power_supply = db.Column(db.String(255))
    battery = db.Column(db.String(255))
    voltage_setting = db.Column(db.Float)
    ovp = db.Column(db.Float)
    current_setting = db.Column(db.Float)
    current_limit = db.Column(db.Float)
    red_green_current_limits = db.Column(db.String(255))
    red_green_voltage_limits = db.Column(db.String(255))

    def json(self):
        return {'id': self.id, "power_supply": self.power_supply, 'battery': self.battery, 'voltage_setting': self.voltage_setting, 'ovp': self.ovp, 'current_setting': self.current_setting, 'current_limit': self.current_limit, 'red_green_voltage_limits': self.red_green_voltage_limits, 'red_green_current_limits': self.red_green_current_limits}
