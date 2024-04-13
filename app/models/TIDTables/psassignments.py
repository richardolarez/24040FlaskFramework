from app import db

class PowerSupplyAssign(db.Model):
    __tablename__ = "PowerSupplyAssign"
    id = db.Column(db.Integer, primary_key=True)
    projectID = db.Column(db.Integer)
    power_supply = db.Column(db.String(255))
    battery = db.Column(db.String(255))
    devices = db.Column(db.String(255))
    ext_pwr = db.Column(db.String(255))
    batt_chg = db.Column(db.String(255))
    control = db.Column(db.String(255))
    monitor = db.Column(db.String(255))

    def json(self):
        return {'id': self.id, "power_supply": self.power_supply, 'battery': self.battery, 'devices': self.devices, 'ext_pwr': self.ext_pwr, 'batt_chg': self.batt_chg, 'control': self.control, 'monitor': self.monitor}
    