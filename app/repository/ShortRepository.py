# from app.interfaces.abstractRepositoryDB import repositoryAbstractGeneric
# from app import db
# from app.models.ShortVideos import ShortVideoMain

# class Short_VRepo(repositoryAbstractGeneric):
#     def get_all(self):
#         return db.session.query(ShortVideoMain).all()
    
#     def get_by_id(self, id_object):
#         return db.session.query(ShortVideoMain).filter_by(id_object).first()
    
#     def create_object(self, short_v):
#         db.session.add(short_v)
#         db.session.commit()
#         return short_v
    
#     def update_object(self, newshort_v):
#         db.session.merge(newshort_v)
#         db.session.commit()
#         return newshort_v
    
#     def delete_object(self, short_v):
#         db.session.delete(short_v)
#         db.session.commit()

    # agregar sentencias adicionales como los likes, comentarios, repost, entre otros
