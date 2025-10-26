
from app.interfaces.abstractRepositoryDB import repositoryAbstractGeneric
from app import db
from app.models.Perfil import PerfilMain

class PerfilRepo(repositoryAbstractGeneric):

    def get_all(self):
        return db.session.query(PerfilMain).all()
    
    def get_by_id(self, id_object):
        return db.session.query(PerfilMain).filter_by(id=id_object).first()
    
    def create_object(self, perfil):
        db.session.add(perfil)
        db.session.commit()
        return perfil
    
    def update_object(self, perfil):
        db.session.merge(perfil)
        db.session.commit()
        return perfil
    
    def delete_object(self):
        db.session.delete()
        db.session.commit()
    
    # obtener referencia del perfil por medio del id de un usuario existente
    def nexo_iduser_perfil(self, iduser):
        return db.session.query(PerfilMain).filter_by(id_user_fk=iduser).first()

    # funciones secundarias del repositorio perfil (seguidores, publicaciones, variados)
    def find_perfil_by_namep(self, name):
        text = f"%{name}%"
        return db.session.execute(
            db.select(PerfilMain).where(PerfilMain.name_perfil.ilike(text))
        ).scalars().all()