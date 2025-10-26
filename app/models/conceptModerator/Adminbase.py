from app import db

class AdminMain(db.Model):
    id_admin = db.Column(db.Integer, primary_key = True)

    def __repr__(self):
        return f'<User {self.username}>'