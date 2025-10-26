# Eliminar todos los message dirigidos en los diccionarios que disponen los metodos 
# al retornar una acción como respuesta

# agregar en la opción de edicion de cada entidad el atributo de date_update para tener un registro de las actualizaciones 

# RECORDAR EL USO DEL BLOQUE TRY



from datetime import date

# llamado a los diferentes repositorios
from app.repository.UserRepository import UserRepo
from app.repository.GroupRepository import GroupRepo
from app.repository.AVRepository import AGRepo
from app.repository.VideoRepository import VideoRepo
# from app.repository.ShortRepository import Short_VRepo
from app.repository.PerfilRepository import PerfilRepo
# from app.repository.

# llamado a los sub servicios necesarios
from app.services.entity_predefinidos.ServicesIntegralUser import UserServicesRestoras

# llamado a los modelos involucrados
from app.models.Userbase import UserDoMain
from app.models.Groupsbase import GroupBase
from app.models.AgenteVirtualBase import AgenteVirtualMain
from app.models.Video import VideoMain 
from app.models.Perfil import PerfilMain

# definir los servicios de la clase grupo:
class UserServicesMain():
    def __init__(self):
        self.repositorio = UserRepo()
        self.repoExtencionUser = UserServicesRestoras()

    # definicion del servicio de generacion de usuario
    def agregar_usuario(self, data):
        # implementar logicas de verificacion (contraseña y existencia [name y email])
        password_hash = self.repoExtencionUser.encriptarClave(data['password'])
        user = UserDoMain(nameuser=data['nameuser'], email=data['email'], password=password_hash)
        self.repositorio.create_object(user)
        return user

    # Este será nuestro punto de partida para ingresar al login con un dashboard
    def ingresar_usuario(self, data):
        pass

    # sección de listas para la entidad user
    # ATENCION A ESTE METODO: pienso que seria exclusivo para los admins (mostrarlo en una tabla) 
    # este metodo se encarga de mostrar una lista <JSON> de los usuarios existentes
    def lista_usuario(self):
        return self.repositorio.get_all()

    # para realizar busquedas en la plataforma
    def lista_usuario_by_name(self, nameuser):
        return self.repositorio.get_by_name_user(nameuser)

    # metodo encargado de buscar el usuario
    # tendra una aplicacion muy diferente (puede ser a la hora de consultar a x perfil)
    def buscar_usuario(self, id_user):
        return self.repositorio.get_by_id(id_user)

    # metodo encargado de editar los componentes necesarios del usuario
    def editar_usuario(self, user, data):
        # implementar sub logica que permite comparar la existencia de estos componentes
        if 'nameuser' in data:
            user.nameuser = data['nameuser']

        if 'email' in data:
            user.email = data['email']

        if 'password' in data:
            new_password = self.repoExtencionUser.encriptarClave(data['password'])
            user.password = new_password

        self.repositorio.update_object(user)
        return user

    # ATENCION A ESTE METODO: pienso que seria exclusivo para los admins
    # metodo encargado de eliminar el usuario por una id 
    def eliminar_usuario(self, user):
        self.repositorio.delete_object(user)
        return{'message': "se ha eliminado el usuario"}
    
    # ATENCIÓN: en esta parte se aloja la logica de atención a los servicios de comprobacion
    def comprobate_email_real(self, email):
        return self.repositorio.get_by_email(email)

# definir los servicios de la clase perfil:
class PerfilServicesMain():
    def __init__(self):
        self.repositoryPerfil = PerfilRepo()

    def agregar_perfil(self, data):
        dateCreate = date.today()
        perfil = PerfilMain(name_perfil=data['name_perfil'], date_creation=dateCreate, label_perfil=data['label_perfil'], description_perfil=data['description_perfil'], img_perfil=data['img_perfil'], img_portada_perfil=data['img_portada_perfil'])
        return self.repositoryPerfil.create_object(perfil)

    def obtener_lista_perfil(self):
        return self.repositoryPerfil.get_all()

    def obtener_perfil_id(self, id_perfil):
        return self.repositoryPerfil.get_by_id(id_perfil)
    
    def obtener_perfil_namep(self):
        pass

    # un metodo usado para ser usado en doble sentido (admin y el mismo usuario) <tendrá doble ruta>
    def editar_perfil(self, perfil, data):
        newDateUpdate = date.today()
        perfil.date_creation = newDateUpdate # agregar como un nuevo atributo en la entidad
        if 'name_perfil' in data:
            perfil.name_perfil = data['name_perfil']

        if 'label_perfil' in data:
            perfil.label_perfil = data['label_perfil']

        if 'description_perfil' in data:
            perfil.description_perfil = data['description_perfil']

        if 'img_perfil' in data:
            perfil.img_perfil = data['img_perfil']

        if 'img_portada_perfil' in data:
            perfil.img_portada_perfil = data['img_portada_perfil']

        self.repositoryPerfil.update_object(perfil)
        return perfil

    # un metodo usado para ser usado en doble sentido (admin y el mismo usuario) <tendrá doble ruta
    def eliminar_perfil(self, id_perfil):
        perfil = self.obtener_perfil_id(id_perfil)
        if perfil in None:
            return {
                'message': f"El perfil con id {id_perfil} no existe"
            }
        
        self.repositoryPerfil.delete_object(perfil)
        return{
            'message': f"se ha eliminado el perfil con id {id_perfil} extinta"
        }

# definir los servicios de la clase grupo:

class GroupServicesMain():
    def __init__(self):
        self.repositoryGroup = GroupRepo()

    def agregar_grupo(self, data, id_perfil):
        fecha = date.today()
        group = GroupBase(name_group=data['name_group'], description_group=data['description_group'], date_creation_group=fecha, id_creator_group_fk=id_perfil) # falta la relacion con el perfil
        self.repositoryGroup.create_object(group)
        return group

    def lista_grupos(self):
        return self.repositoryGroup.get_all()
    
    def obtener_grupo_nameg(self, namegroup):
        return self.repositoryGroup.find_grupo_by_nameg(namegroup)

    def obtener_grupo_id(self, id_grupo):
        return self.repositoryGroup.get_by_id(id_grupo)

    def editar_grupo(self, grupo, data):
        # opciones faltantes 
        if 'name_group' in data:
            grupo.name_group = data['name_group']

        if 'description_group' in data:
            grupo.description_group = data['description_group']
        
        self.repositoryGroup.update_object(grupo)
        return grupo
        
    def eliminar_grupo(self, id_grupo):
        grupo = self.repositoryGroup.get_by_id(id_grupo)
        if grupo is None:
            return {
                'message': f"el grupo con la id {id_grupo} no existe"
            }
        pass

    # enlazar el id del usuario que creo el grupo

# definir los servicios de videos
class VideosServicesMain():
    def __init__(self):
        self.repositoryVideo = VideoRepo()
    def obtener_lista_videos(self):
        return self.repositoryVideo.get_all()

    def obtener_video_id(self, id_video):
        return self.repositoryVideo.get_by_id(id_video)

    def agregar_video(self, data):
        video = VideoMain(title_video=data['title_video'], description_video=data['description_video'], publication_date_video=data['publication_date_video'], miniatura_video=data['miniatura_video'])
        return self.repositoryVideo.create_object()

    def actualizar_video(self, id_video, newdata):
        video = self.repositoryVideo.get_by_id(id_video)
        if video is None:
            return {
                'message': f"el video a consultar no existe con id {id_video}"
            }
        
        # if newdata['title_video'] is not None:
        #     video.title_video = newdata.get('title_video', video.title_video)

        # if newdata['description_video'] is not None:
        #     video.description_video = newdata.get('description_video', video.description_video)

        # if newdata['publication_date_video'] is not None:
        #     video.publication_date_video = newdata.get('publication_date_video', video.publication_date_video)

        # if newdata['miniatura_video'] is not None:
        #     video.miniatura_video = newdata.get('miniatura_video',  video.miniatura_video)
        
        self.repositoryVideo.update_object(video)
        return video # sus demas atributos constan de total independencia en esta unidad
    
    def eliminar_video(self, id_video):
        video = self.repositoryVideo.get_by_id(id_video)
        if video is None:
            return 0
        
        self.repositoryVideo.delete_object(video)
        return {
            'message': f"se ha eliminado el video con id extinta: {id_video}"
        }


# definir los servicios de shots
# class ShortServicesMain():
#     def __init__ (self):
#         self.repositoryShort = Short_VRepo()

#     def obtener_lista_short(self):
#         return self.repositoryShort.get_all()

#     def obtener_short_id(self, id_short):
#         return self.repositoryShort.get_by_id(id_short)

#     def agregar_short(self, data):
#         date_publication = date.today()
#         short = ShortVideoMain(title_short=data['title_short'], description_short=data['description_short'], publication_date_short=date_publication, miniatura_short=data['miniatura_short'])
#         return self.repositoryShort.create_object(short)

#     def actualizar_short(self, short, newshort):
#         # aqui tenemos un espacio en donde 
#         if 'title_short' in newshort:
#             short.title_short = newshort['title_short']

#         if 'description_short' in newshort:
#             short.description_short = newshort['description_short']

#         if 'miniatura_short' in newshort:
#             short.miniatura_short = newshort['miniatura_short']

#         self.repositoryShort.update_object(short)
#         return short


#     def eliminar_short(self, id_short):
#         short = self.obtener_short_id(id_short)
#         if short is None:
#             return{
#                 'message': f"El short con id {id_short} no existe"
#             }
#         self.repositoryShort.delete_object(short)
#         return {
#             'message': "el short se ha eliminado"
#         }

# definir los servicios de AG
class AVServicesMain():
    def __init__(self):
        self.repositoryAG = AGRepo()

    def obtener_AV(self):
        return self.repositoryAG.get_all()

    def obtener_AV(self, id_av):
        return self.repositoryAG.get_by_id(id_av)

    def agregar_AV(self, data):
        avmain = AgenteVirtualMain(type_agent=data['type_agent'], level_access=data['level_access'], status_agent=data['status_agent']) # falta configurar la parte de los status de agente
        return avmain

    def actualizar_AV(self, avmain, newdata):
        
        if 'type_agent' in newdata:
            avmain.type_agent = newdata['type_agent']

        if 'level_access' in newdata:
            avmain.level_access = newdata['level_access']

        if 'status_agent' in newdata:
            avmain.status_agent = newdata['status_agent']

        self.repositoryAG.update_object(avmain) # como se asegura de poder agregar una funcion estable y funcional en esta linea?
        return avmain

    def eliminar_AV(self, avmain):
        self.repositoryAG.delete_object(avmain)
        return {'message': "el agente virtual ha sido eliminado"}
    
    # agregar la clases de mensaje y chat (tienen tambien una relación con el grupo)

    class MessageServicesMain():
        # funciones que debe tener el mensage = crearlo, buscarlo, editarlo y eliminarlo (este ultimo tendrá su logica)
        pass

    # mirar la relacion que existe en la matriz de cardinalidad
    class ChatServicesMain():
        # debe de relacionar al los perfiles en un espacio en donde estos puedan mandar mensajes (a los sumo debe de contar con 2 perfiles para que funcione)
        # este tambien almacenará los distintos mensajes que se enviaran 
        pass

    class Publicaciones():
        # debemos establecer primero el lugar en donde se expondrán estas publicaciones 
        # tiene una relación con los principales formatos (videos y shorts), y tambien podemos contar con una descripcion de la publicación
        pass

    # revisar la cuestion de los seguidores en la BD
    class followerServicesMain():
        pass

    class NotifyServicesMain():
        pass
