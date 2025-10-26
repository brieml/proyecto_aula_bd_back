from app import db

class VideoMain(db.Model):
    __tablename__ = 'video'
    id_video = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title_video = db.Column(db.String(60), unique=True, nullable=False)
    description_video = db.Column(db.String(255), unique=False, nullable=True)
    publication_date_video = db.Column(db.Date, unique=False, nullable=False)
    miniatura_video = db.Column(db.String(255), unique=True, nullable=False) # aqui se encuentra la dirección de la img miniatura
    like_video = db.Column(db.Integer, unique=True, nullable=False) #implementar logica especial en la sección de likes

    # establecer relacion con publicación

    def __repr__(self):
        return f'<user {self.title_vide0}>'