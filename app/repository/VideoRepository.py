from app.interfaces.abstractRepositoryDB import repositoryAbstractGeneric
from app import db
from app.models.Video import VideoMain

class VideoRepo(repositoryAbstractGeneric):
    
    def get_all(self):
        return db.session.query(VideoMain).all()    
    def get_by_id(self, id_object):
        return db.session.query(VideoMain).filter_by(id_object).first()
    
    def create_object(self, video):
        db.session.add(video)
        db.session.commit()
        return video
    
    def update_object(self, newVideo):
        db.session.merge(newVideo)
        db.session.commit()
        return newVideo
    
    def delete_object(self, video):
        db.session.delete(video)
        db.session.commit()
    
    # agregar sentencias adicionales como los likes, comentarios, repost, entre otros