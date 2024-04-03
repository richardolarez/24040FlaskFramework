from app import db

class Component(db.Model):
    __tablename__ = "Component"
    componentId = db.Column(db.Integer, primary_key=True)
    projectId = db.Column(db.Integer)
    componentName = db.Column(db.String(255))
    partNumber = db.Column(db.String(255))

    def json(self):
        return {'id': self.id, 'name': self.name, 'PN': self.PN}

    def __init__(self, name, ID, PN):
        self.name = name
        self.componentId = ID 
        self.partNumber = PN