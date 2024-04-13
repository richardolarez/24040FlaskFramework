from app import db

class PowerSupply(db.Model):
    __tablename__ = "PowerSupply"

    id = db.Column(db.Integer, primary_key=True)
    projectID = db.Column(db.Integer)
    power_supply = db.Column(db.String(255))
    battery_system = db.Column(db.String(255))
    voltage_setting = db.Column(db.Float)
    ovp = db.Column(db.Float)
    current_limit = db.Column(db.Float)
    red_green_current_limits = db.Column(db.String(255))
    red_green_voltage_limits = db.Column(db.String)

    def json(self):
        return {'id': self.id, "power_supply": self.power_supply, 'battery_system': self.battery_system, 'voltage_setting': self.voltage_setting, 'ovp': self.ovp, 'current_limit': self.current_limit, 'red_green_voltage_limits': self.red_green_voltage_limits, 'red_green_current_limits': self.red_green_current_limits}