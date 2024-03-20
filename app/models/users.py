from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    # def json(self):
    #     return {'id': self.id, 'username': self.username, 'password': self.password, 'email': self.email, 'role': self.role}