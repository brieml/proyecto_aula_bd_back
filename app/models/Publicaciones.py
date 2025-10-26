from app import db 

class PostMain(db.Model):
    #
    # like publicacion puede contar con un contador y a su vez puede tener una logica de patron booleana
    # tiene que ser un usuario que contemple la opcion booleana si tiene un like o no
    # este tendra la opcion de agregar o eliminar 1 la cuenta del like
    # #    
    id_publicaciones = db.Column(db.Integer, primary_key = True, autoincrement=True)
    date_publicacion = db.Column(db.Date, unique=False, nullable=False)
    descripcion_publicacion = db.Column(db.Text, unique=False, nullable=False)
    # formato_publicacion # <-- hablar sobre este atributo

    url_contenido = db.Column(db.String(255), unique=True, nullable=False) # se sabe que las url que se generan son unicas
    like_publicacion = db.Column(db.Integer, unique=False, nullable=False)
    comentarios_publicacion = db.Column(db.String(255), unique=False, nullable=True) # hablar sobre estas entidad
    # id_publicacion_padre  # <-- hablar sobre este atributo 

