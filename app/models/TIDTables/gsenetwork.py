from app import db

class GSENetwork(db.Model):
    __tablename__ = "GSENetwork"
    id = db.Column(db.Integer, primary_key=True)
    projectID = db.Column(db.Integer)
    gse_net_device = db.Column(db.String(255))
    ip_address = db.Column(db.String(255))
    sub_net_mask = db.Column(db.String(255))
    host_name = db.Column(db.String(255))

    def json(self):
        return {'id': self.id, 'gse_net_device': self.gse_net_device, 'ip_address': self.ip_address, 'sub_net_mask': self.sub_net_mask, 'host_name': self.host_name}