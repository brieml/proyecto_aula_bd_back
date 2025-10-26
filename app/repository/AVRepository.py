from app.interfaces.abstractRepositoryDB import repositoryAbstractGeneric
from app import db
from app.models.AgenteVirtualBase import AgenteVirtualMain

class AGRepo(repositoryAbstractGeneric):
    pass
    def get_all(self):
        return db.session.query(AgenteVirtualMain).all()
    
    def get_by_id(self, id_object):
        return db.session.query(AgenteVirtualMain).filter_by(id_object).first()
    
    # una forma de crear registrar las entidades que se utilizan en la aplicación
    def create_object(self, avmodel):
        db.session.add(avmodel)
        db.session.commit()
        return avmodel
    
    def update_object(self, newAVm):
        db.session.merge(newAVm)
        db.session.commit()
        return newAVm
    
    def delete_object(self, avmodel):
        db.session.delete(avmodel)
        db.session.commit()
    
    # funciones de entrega, edición y eliminación al agente (preguntas, imgs, entre otros materiales)
