from app import db

class Component(db.Model):
    __tablename__ = "Component"
    componentId = db.Column(db.String(255), primary_key=True)
    projectId = db.Column(db.Integer, primary_key=True)
    componentName = db.Column(db.String(255))
    partNumber = db.Column(db.String(255))
    componentType = db.Column(db.String(255))

    def json(self):
        return {'componentId': self.componentId, 'projectId': self.projectId, 'componentName': self.componentName, 'partNumber': self.partNumber, 'componentType': self.componentType}