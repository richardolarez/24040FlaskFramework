from app import db
class Battery(db.Model):
    __tablename__ = "Battery"
    batteryId = db.Column(db.String(255), primary_key=True)
    projectId = db.Column(db.Integer)
    name = db.Column(db.String(255))
    partNumber = db.Column(db.String(255))

    def json(self):
        return {'id': self.batteryId, 'name': self.name, 'PN': self.partNumber}

    def __init__(self, name, ID, partNumber):
        self.name = name
        self.batteryId = ID 
        self.partNumber = partNumber
        