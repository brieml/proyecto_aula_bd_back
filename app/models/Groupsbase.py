
from app import db

class GroupBase(db.Model):
    __tablename__ = 'grupo'
    id_group = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_group = db.Column(db.String(60), unique=True, nullable=False)
    description_group = db.Column(db.String(255), unique=False, nullable=False)
    date_creation_group = db.Column(db.Date, unique=False, nullable=False)

    id_creator_group_fk = db.Column(db.Integer, db.ForeignKey('perfil.id_perfil'), nullable=False) 
    
    # Nombre de la propiedad de relación en GroupBase es 'memberships'
    # back_populates apunta a la propiedad 'group' en GroupMember.
    memberships = db.relationship('GroupMember', back_populates='group', lazy='dynamic')

    def __repr__(self):
        return f'<Group {self.name_group}>'

# a las entidades Principales (en este caso perfil, no deben de tener tablas intermedias en su archivo)
# en este caso, la entidad grupo tiene que tener una tabla intermedia para relacionarlas con perfil 
# TABLA DE RELACION PERFIL - GRUPOS (N:M)
class GroupMember(db.Model):
    __tablename__ = 'miembro_grupo'
    
    id_perfil_fk = db.Column(db.Integer, db.ForeignKey('perfil.id_perfil'), primary_key=True)
    id_group_fk = db.Column(db.Integer, db.ForeignKey('grupo.id_group'), primary_key=True)
    date_register_member = db.Column(db.Date, unique=False, nullable=False)
    
    # Nombre de la propiedad de relación en GroupMember es 'group'
    # back_populates apunta a la propiedad 'memberships' en GroupBase.
    group = db.relationship('GroupBase', back_populates='memberships')
    
    # Nombre de la propiedad de relación en GroupMember es 'profile'
    # back_populates apunta a la propiedad 'grupos' en PerfilMain.
    profile = db.relationship('PerfilMain', back_populates="grupos")
