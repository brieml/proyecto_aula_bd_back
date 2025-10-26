from app import ma
from app.models.Userbase import UserDoMain
from app.models.Groupsbase import GroupBase
from app.models.conceptModerator.Adminbase import AdminMain
from app.models.Perfil import PerfilMain
from app.models.AgenteVirtualBase import AgenteVirtualMain
from app.models.Video import VideoMain
# from app.models.Chat import 

#esquema de la clase usuario
class UserSchemaArtefact(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserDoMain
        load_instance = True

user_schema = UserSchemaArtefact()
users_schema = UserSchemaArtefact(many=True)

#esquema de la clase grupos/comunidades
class GroupSchemaArtefact(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GroupBase
        load_instance = True

group_schema = GroupSchemaArtefact()
groups_schema = GroupSchemaArtefact(many=True)

#esquema de la clase perfil
class PerfilSchemaArtefact(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PerfilMain
        load_instance = True

perfil_schema = PerfilSchemaArtefact()
perfiles_schema = PerfilSchemaArtefact(many=True)

#esquema de la clase AgentesVirtuales
class VirtualAgentSchemaArctefact(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AgenteVirtualMain
        load_instance = True

AV = VirtualAgentSchemaArctefact()
AsVs = VirtualAgentSchemaArctefact(many=True)

#esquema de la clase video
class VideoSchemaArtefact(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VideoMain
        load_instance = True

video_schema = VideoSchemaArtefact()
videos_schema = VideoSchemaArtefact(many=True)

#esquema de la clase short
class ShortSchemaArtefact(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VideoMain
        load_instance = True

short_schema = ShortSchemaArtefact()
shorts_schema = ShortSchemaArtefact(many=True)

class ChatSchemaArtefact(ma.SQLAlchemyAutoSchema):
    class Meta:
        pass 

# seccion de privilegios

#esquema de la clase admin
class AdminSchemaArtefact(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AdminMain
        load_instance = True

admin_schema = AdminSchemaArtefact()
admins_schema = AdminSchemaArtefact(many=True)

