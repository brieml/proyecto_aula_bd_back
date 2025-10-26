from app import db

class ChatMain(db.Model):
    __tablename__ = 'chat'
    id_chat = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_creation_chat = db.Column(db.Date, unique=False, nullable=False)
    is_group = db.Column(db.Boolean, unique=False, nullable=False)

    id_mensaje_fk = db.Column(db.Integer, db.ForeignKey('mnesaje'), unique=False, nullable=False)
    chat_participante = db.relationship('ChatParticipante', back_populates='chat', lazy='dynamic')

class ChatParticipante(db.Model):
    __tablename__ = 'chat_perfil'
    id_chat_fk = db.Column(db.Interger, db.ForeignKey(''), unique=False, nullable=False)
    id_perfil_fk = db.Column(db.Integer, db.ForeignKey(''), unique=False, nullable=False)

    #referencias de las otras tablas
    chat = db.relationship('ChatMain', back_populates='chat_participante')
