from app.interfaces.abstractRepositoryDB import repositoryAbstractGeneric
from app import db
from app.models.Groupsbase import GroupBase

class GroupRepo(repositoryAbstractGeneric):
    
    def get_by_id(self, id_object):
        return db.session.query(GroupBase).filter_by(id=id_object).first()
    
    def get_all(self):
        return db.session.query(GroupBase).all()
    
    def create_object(self, grupo):
        db.session.add(grupo)
        db.session.commit()
        return grupo
    
    def update_object(self, grupo):
        db.session.merge(grupo)
        db.session.commit()
        return grupo
    
    def delete_object(self, grupo):
        db.session.delete(grupo)
        db.session.commit()

    # metodo auxiliares para la busqueda de los grupos por su nombre
    def find_grupo_by_nameg(self, name):
        text = f"%{name}%"
        return db.session.query(GroupBase.name_group.ilike(text)).all()
    
    # extras de la entidad
    def get_all_perfil(self):
        pass

    def add_perfil_group(self, perfil):
        pass

    def expul_perfil_group():
        pass

    # agregar opciones que juegan un papel bajo las funciones de la entidad grupo y que afectan a los perfiles 
    # se define como lo siguiente: agregar un sub rol dentro de los grupos owner y mod