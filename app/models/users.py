from app import db

class User(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255))
    role = db.Column(db.String(255))

    # def json(self):
    #     return {'id': self.id, 'username': self.username, 'password': self.password, 'email': self.email, 'role': self.role}