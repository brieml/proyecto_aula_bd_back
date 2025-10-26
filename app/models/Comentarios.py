from app import db

class ComentarioMain(db.Model):
    id_comentarios = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_comentario = db.Column(db.Date, unique=False, nullable=False)
    date_state_update_comentaio = db.Column(db.Boolean, unique=False, nullable=False) # <-- dependiendo del tipo de comentario se le asigna un tiempo al backend 
    contenido_comentario = db.Column(db.Text, unique=False, nullable=True)
    tipo_contenido = db.Column(db.Enum, unique=False, nullable=False)
    
    # id_contenido
    # id_perfil_fk