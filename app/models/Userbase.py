from app import db
from flask_login import UserMixin

#
# Inscribir Ids dinamicos para los usarios o perfiles
# #
class UserDoMain(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nameuser = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False) # cambiar a 255 
    is_activate = db.Column(db.Boolean, default=True) # la informaciòn se traslada por medio de usermixin

    # relaciones de la entidad con otros
    perfil = db.relationship('PerfilMain', backref='users', uselist=False, lazy='joined')

    def __repr__(self):
        return f'<user {self.nameuser}>'