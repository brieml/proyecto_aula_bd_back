# aqui se van a usar las vistas del template propios del dashboard
# esta seccion solo pueden entablar servicios si el usuario es una instancia de flask_login (current_user)
from flask import Blueprint, render_template, url_for, request, jsonify, flash, redirect
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_login import login_required, current_user

# from app.models.Groupsbase import GroupBase
from app.services.ServicesBase import GroupServicesMain, UserServicesMain
from app.services.auth.authservices import LoginServicesMain
from app.repository.PerfilRepository import PerfilRepo
from app.schemas.Schemas import group_schema, groups_schema
from datetime import datetime

api_view_dashboard = Blueprint('dashboard', __name__)
group_services = GroupServicesMain()
perfil_repo = PerfilRepo()

# ENDPOINT: esto es para la salida de la seccion del usuario
@api_view_dashboard.route('/logout', methods=['GET'])
@login_required # <-- será despresiado 
# quiere decir que requiere la seccion para realizar estas funciones
def logout_user():
    # permite cerrar la seccion de la cuenta
    LoginServicesMain.back_account_user()
    flash('Haz salido de la cuenta con exito', 'info')
    return render_template('salida.html') # <-- agregar redireccion a esto?

# ATENCION: este endpoint es solo de prueba
# seccion principal o seccion base del perfil

@api_view_dashboard.route('/main')
@login_required
# @jwt_required()
def view_index_dashboard():
    return render_template('index.html')

    # try:
    #     return render_template('index.html')
    # except Exception as error_view:
    #     return jsonify({
    #         'message_error_view': "error al cargar la vista en cuestion",
    #         'causa': f"{error_view}"
    #     }), 400

# ATENCION: a continuacion, se alojaran las vistas secundarias del dashboard

# seccion de descripcion (aqui el perfil encuentra la vista de su perfil, aqui puede observar sus descripcion, foto, img, datos, entre otros)
# ATENCION: MOVER ESTA LOGICA A SU RESPECTIVO CONTROLLER
# seccion de crear grupos (aqui el perfil puede crear sus grupos)
@api_view_dashboard.route('/create/group', methods=['POST'])
@login_required
# @jwt_required() # una opcion mas segura que login_required
def create_space_group():
    # current_id_perfil = get_jwt_identity() # <-- al tener una token, este devuelve la referencia del usuario que esta accediendo
    perfil_id = perfil_repo.nexo_iduser_perfil(current_user.id)
    data = request.get_json()

    # definicion de los parametros necesarios
    if _comprobate(nombreGroup=data['name_group'], descripcionGroup=data['description_group']):
        return jsonify({'message': "faltan campos por llenar dentro de la creacion de grupos"}), 400
    
    # crear una opcion para comprobar si ese grupo existe con un nombre
    
    new_group = group_services.agregar_grupo(data=data, id_perfil=perfil_id.id_perfil)
    return jsonify(group_schema.dump(new_group))

    # crear la instancia de la clase y devolverla al servicio del mismo

# seccion de grupos encontrados por medio de su nombre
@api_view_dashboard.route('/search/group', methods=['GET'])
@login_required
# @jwt_required()
def search_name_group():
    data = request.get_json()
    groups = group_services.obtener_grupo_nameg(namegroup=data['name_groups'])
    return jsonify(groups_schema.dump(groups))

# seccion de grupos publicos recomendados
@api_view_dashboard.route('/group', methods=['GET'])
@login_required
# @jwt_required()
def all_groups():
    groups = group_services.lista_grupos()
    return jsonify(groups_schema.dump(groups)), 200

# seccion de chats registrados (aqui el perfil puede ver un historial de las personas que ha chateado)

# seccion de publicacion (esta seccion puede proporcionar dos vistas; una que se encarga de subir reals y la otra de videos con distinto formato)

# acceso a la seccion publica de las publicaciones tipo reals

# acceso a la seccion publica de videos y shots

# espacio de metodos privados
def _comprobate(nombreGroup, descripcionGroup):
    return True if(not nombreGroup or not descripcionGroup) else False


