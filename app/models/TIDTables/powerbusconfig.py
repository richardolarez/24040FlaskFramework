from app import db

class PowerBusConfig(db.Model):
    __tablename__ = "PowerBusConfig"
    id = db.Column(db.Integer, primary_key=True)
    projectID = db.Column(db.Integer)
    power_supply = db.Column(db.String(255))
    battery = db.Column(db.String(255))
    component = db.Column(db.String(255))
    ext_pwr = db.Column(db.String(255))
    int_pwr = db.Column(db.String(255))
    bus_v_low = db.Column(db.String(255))
    bus_v_high = db.Column(db.String(255))
    bus_i_low = db.Column(db.String(255))
    bus_i_high = db.Column(db.String(255))

    def json(self):
        return {'id': self.id, "power_supply": self.power_supply, 'battery': self.battery, 'component': self.component, 'ext_pwr': self.ext_pwr, 'int_pwr': self.int_pwr, 'bus_v_low': self.bus_v_low, 'bus_v_high': self.bus_v_high, 'bus_i_low': self.bus_i_low, 'bus_i_low': self.bus_i_high}
    