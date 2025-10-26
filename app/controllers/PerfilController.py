from flask import Blueprint, request, jsonify
from app.services.ServicesBase import PerfilServicesMain
from app.schemas.Schemas import perfil_schema, perfiles_schema


perfil_api = Blueprint('perfil_main', __name__)
perfil_services = PerfilServicesMain()

# metodo protegido por los servicios de admin
@perfil_api.route('/todo_perfil', methods=['GET'])
def PerfilAll():
    perfiles = perfil_services.obtener_lista_perfil()
    return jsonify(perfiles_schema.dump(perfiles))

# metodo protegido por los servicios de admin
@perfil_api.route('/find/<int:id_perfil>', methods=['GET'])
def Perfil_by_id(id_perfil):
    perfil = perfil_services.obtener_perfil_id(id_perfil)
    if not perfil:
        return jsonify({'message': f"No se ha encontrado el perfil con la id {id_perfil}"}), 401
    return jsonify(perfil_schema.dump(perfil)), 201

@perfil_api.route('/nameperfil/<name_perfil>', methods=['GET'])
def perfil_by_name(name_perfil):
    perfiles = perfil_services.obtener_perfil_namep(name_perfil)
    if not perfiles:
        return jsonify({'message': f"No existen perfiles con el nombre de {name_perfil}"})
    return jsonify(perfiles_schema.dump(perfiles))

# metodo publico para el usuario
# URGENTE: este metodo hace parte de las bases del login, por lo que se puede ver afectado más adelante
@perfil_api.route('/create', methods=['POST'])
def PerfilCreate():
    data = request.get_json()
    errors = perfil_schema.validate(data)
    if errors:
        return jsonify(errors), 400 # encontrar una forma de clasificar errores
    new_perfil = perfil_services.agregar_perfil(data)
    return jsonify(perfil_schema.dump(new_perfil))

# metodo publico para el usuario (tendrá una referencia automatica al iniciar seccion)
# @perfil_api.route()
# def update_perfil_personal():
#     pass

# metodo publico para el usuario (tendrá una referencia automatica al iniciar seccion)
# @perfil_api.route()
# def delete_perfil_personal():
#     pass

# metodo protegido por los servicios de admin
@perfil_api.route('/perfils/<int:id_perfil>', methods=['PATCH'])
def Perfil_update_admin(id_perfil):
    data = request.get_json()
    oldPerfil = perfil_services.obtener_perfil_id(id_perfil)
    if not oldPerfil:
        return jsonify({'message': f"No se ha encontrado el perfil con la id {id_perfil}"})
    
    new_perfil = perfil_services.editar_perfil(oldPerfil, data)
    return jsonify(perfil_schema.dump(new_perfil))


# la relacion de eliminacion puede variar en el sentido de que es lo que se estará eliminando (dentro del contexto de perfil-usario)
# metodo protegido por los servicios de admin
@perfil_api.route('/perfils/<int:id_perfil>', methods=['DELETE'])
def Perfil_delete_admin(id_perfil):
    perfil = perfil_services.obtener_perfil_id(id_perfil)
    if not perfil:
        return jsonify({'message': f"No se ha encontrado el perfil con la id {id_perfil}"}), 400
    action_delete = perfil_services.eliminar_perfil(perfil)
    return jsonify(action_delete), 201
