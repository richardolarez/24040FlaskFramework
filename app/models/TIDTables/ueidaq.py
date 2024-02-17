from app import db

class UEIDaq(db.Model):
    __tablename__ = "UEIDaq"
    id = db.Column(db.Integer, primary_key=True)
    power_daq_layer = db.Column(db.String(255))
    bit = db.Column(db.String(255))
    pin = db.Column(db.String(255))
    signal = db.Column(db.String(255))
    initial = db.Column(db.String(255))

    def json(self):
        return {'id': self.id, 'power_daq_layer': self.power_daq_layer, 'bit': self.bit, 'pin': self.pin, 'signal': self.signal, 'initial': self.initial}