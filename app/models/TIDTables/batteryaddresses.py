from app import db


class BatteryAddresses(db.Model):
    __tablename__ = "BatteryAddresses"
    id = db.Column(db.Integer, primary_key=True)
    battery = db.Column(db.String(255))
    rs485_address = db.Column(db.String(255))

    def json(self):
        return {'id': self.id, 'battery': self.battery, 'rs485_address': self.rs485_address}
    
