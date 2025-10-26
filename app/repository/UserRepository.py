from app.interfaces.abstractRepositoryDB import repositoryAbstractGeneric
from app import db
from app.models.Userbase import UserDoMain

class UserRepo(repositoryAbstractGeneric):
    
    def get_by_id(self, id_object):
        return db.session.query(UserDoMain).filter_by(id=id_object).first()
    
    def get_all(self):
        return db.session.query(UserDoMain).all()
    
    def create_object(self, user):
        db.session.add(user)
        db.session.commit()
        return user
    
    def update_object(self, user):
        db.session.merge(user)
        db.session.commit()
        return user
    
    def delete_object(self, user):
        db.session.delete(user)
        db.session.commit()

    # repos que son necesarios para la busqueda del usuario (ya sea por medio de su email)
    # metodo usado para llamar a un usuario por medio de su email. Tiene como proposito de encontrar al usuario con su atributo unico
    # a si es, es su email (este me permite verificar su existencia)
    def get_by_email(self, emailuser):
        return db.session.query(UserDoMain).filter_by(email=emailuser).first()
    
    # metodo usado para llamar una lista de usuario por medio de su name
    def get_by_name_user(self, nameUser):
        text = f"%{nameUser}%"
        return db.session.execute(
            db.select(UserDoMain).where(UserDoMain.nameuser.ilike(text))
        ).scalars().all()
    
    # metodo usado para entregar la seccion a un usuario
