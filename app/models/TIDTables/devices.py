from app import db

class Devices(db.Model):
    __tablename__ = "Devices"
    id = db.Column(db.Integer, primary_key=True)
    device = db.Column(db.String(255))

    def json(self):
        return {'id': self.id, 'device': self.device}