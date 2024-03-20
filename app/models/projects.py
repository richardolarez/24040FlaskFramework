from app import db
class Projects(db.Model):
    __tablename__ = "Projects"
    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.String(255))
    tid_tables = db.relationship('TIDTableRelationships', backref='project', lazy='dynamic')

    def json(self):
        return {'id': self.id, 'project': self.project}