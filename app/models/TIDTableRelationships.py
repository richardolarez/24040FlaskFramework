from app import db
class TIDTableRelationships(db.Model):
    __tablename__ = "TIDTables"
    id = db.Column(db.Integer, primary_key=True)
    projectId = db.Column(db.Integer, db.ForeignKey('Projects.id'))
    table = db.Column(db.String(255))

    def json(self):
        return {'id': self.id, 'table': self.table, "projectId": self.projectId}
    