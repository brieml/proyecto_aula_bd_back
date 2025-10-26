from app import db

class PerfilMain(db.Model):
    __tablename__ = 'perfil'
    id_perfil = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_perfil = db.Column(db.String(60), unique=True, nullable=False)
    date_creation = db.Column(db.Date, unique=False, nullable=False)
    label_perfil = db.Column(db.String(255), unique=False, nullable=True)
    description_perfil = db.Column(db.Text, unique=False, nullable=True)
    img_perfil = db.Column(db.String(255), unique=False, nullable=True) # declaración de la ruta de la imagen 
    img_portada_perfil = db.Column(db.String(255), unique=False, nullable=True) # declaración de la ruta de la imagen como portada 

    # relacion con la entidad usuario
    id_user_fk = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False) 
    # creador de grupos (relaciones futuras)
    # Nombre de la propiedad de relación en PerfilMain es 'grupos'
    # back_populates apunta a la propiedad 'profile' en GroupMember.
    grupos = db.relationship('GroupMember', back_populates="profile", lazy='dynamic')
    
    # Asegúrate de que ChatParticipante tiene la propiedad 'perfil'
    # mensajes = db.relationship('ChatParticipante', back_populates="perfil", lazy='dynamic')

    def __repr__(self):
        return f'<user {self.name_perfil}>'
    
