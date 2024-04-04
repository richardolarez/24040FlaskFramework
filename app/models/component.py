from app import db

class Component(db.Model):
    __tablename__ = "Component"
    componentId = db.Column(db.String(255), primary_key=True)
    projectId = db.Column(db.Integer)
    componentName = db.Column(db.String(255))
    partNumber = db.Column(db.String(255))
    componentType = db.Column(db.String(255))

    def json(self):
        return {'id': self.componentId, 'name': self.componentName, 'PN': self.partNumber, 'component': self.componentType}

    def __init__(self, name, ID, PN, componentType):
        self.componentName = name
        self.componentId = ID 
        self.partNumber = PN
        self.componentType = componentType