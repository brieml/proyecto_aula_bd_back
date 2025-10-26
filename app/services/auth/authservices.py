from flask_login import login_user, logout_user 
from flask import flash
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token
from app.repository.UserRepository import UserRepo
from app.repository.PerfilRepository import PerfilRepo
from app.schemas.Schemas import user_schema, perfil_schema
from app.models.Userbase import UserDoMain
from app.models.Perfil import PerfilMain

class LoginServicesMain():
    # metodo 
    def __init__(self):
        self.repoUser = UserRepo()
        self.repoPerfil = PerfilRepo()

    # metodo encargado de realizar la accion de registrar la cuenta y el usuario en la base de datos
    # algoritmo secuencial = se podria consultar el email primero y despues de llenar el perfil y asi guardar los datos

    def register_user(self, data_all):
        password_hash = generate_password_hash(data_all['password'])
        date_perfil = datetime.now()

        user = UserDoMain(nameuser=data_all['nameuser'], email=data_all['email'], password=password_hash)
        self.repoUser.create_object(user)

        new_perfil = PerfilMain(name_perfil=data_all['name_perfil'], date_creation=date_perfil, id_user_fk=user.id)
        self.repoPerfil.create_object(new_perfil)
        # retornar la autenticacion aca para poder entrar a la seccion
        login_user(user)
        flash('Inicio de sesión exitoso [desde register].', 'success')
        # access_token = create_access_token(identity=new_perfil.id_perfil)

        # return access_token
        return {'bool': True,
                    'message': perfil_schema.dump(new_perfil)} # prueba de debug para obtener el perfil
    
    def authenticate_user(self, dateuser):
        userReal = self.repoUser.get_by_email(dateuser['email'])
        if userReal and check_password_hash(userReal.password, dateuser['password']):
            # search_perfil = self.repoPerfil.nexo_iduser_perfil(userReal.id)
            login_user(userReal) # <-- se tiene el inicio de seccion por la cuenta (manejo de coockies o session)
            # access_token = create_access_token(identity=search_perfil.id_perfil)
            referencia_perfil = self.repoPerfil.nexo_iduser_perfil(userReal.id)
            # redireccion de los datos 
            flash('Inicio de sesión exitoso [desde login].', 'success') # presentarle la noticia a flask
            return {'bool': True,
                    'message': perfil_schema.dump(referencia_perfil)} # <-- probar esta adaptacion, me retorna el perfil por medio de la id usuario
            # return access_token
        # return False # solo que es falso si los datos son incorrectos
        return {'bool': False,
                'message': "correo o password invalidos"}

    @staticmethod
    def back_account_user():
        logout_user()