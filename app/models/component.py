from app import db

class Component(db.Model):
    __tablename__ = "Component"
    componentId = db.Column(db.String(255), primary_key=True)
    projectId = db.Column(db.Integer, primary_key=True)
    componentName = db.Column(db.String(255))
    partNumber = db.Column(db.String(255))
    componentType = db.Column(db.String(255))

    def json(self):
        return {'id': self.componentId, 'name': self.componentName, 'PN': self.partNumber, 'component': self.componentType, "projectId": self.projectID}

    def __init__(self, name, ID, PN, componentType, projectID):
        self.componentName = name
        self.componentId = ID 
        self.partNumber = PN
        self.componentType = componentType
        self.projectId = projectID