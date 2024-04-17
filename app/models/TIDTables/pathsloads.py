from app import db

class PathsLoads(db.Model):
    __tablename__ = "PathsLoads"
    id = db.Column(db.Integer, primary_key=True)
    projectID = db.Column(db.Integer)
    power_supply = db.Column(db.String(255))
    battery = db.Column(db.String(255))
    ptm_channel = db.Column(db.String(255))
    components = db.Column(db.String(255))
    current = db.Column(db.Float)
    range_ = db.Column(db.String(255))

    def json(self):
        return {'id': self.id, 'power_supply': self.power_supply, 'battery': self.battery, 'ptm_channel': self.ptm_channel, 'components': self.components, 'current': self.current, 'range_': self.range_}
    
