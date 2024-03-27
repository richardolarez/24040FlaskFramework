from app import db
class AVNetworkSwitchObject(db.Model):
    __tablename__ = "AVNetworkSwitchObject"
    avnId = db.Column(db.Integer, primary_key=True)
    projectID = db.Column(db.Integer)
    name = db.Column(db.String(255))
    PN = db.Column(db.String(255))

    def json(self):
        return {'id': self.id, 'name': self.name, 'PN': self.PN}

    def __init__(self, name, projectID, PN):
        self.name = name
        self.projectID = projectID
        self.PN = PN