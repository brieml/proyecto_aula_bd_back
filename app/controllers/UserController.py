from flask import Blueprint, request, jsonify
from app.services.ServicesBase import UserServicesMain
from app.schemas.Schemas import user_schema, users_schema

user_api = Blueprint('user_main', __name__)
user_services = UserServicesMain()

# metodo protegido por los servicios de admin
@user_api.route('/', methods=['GET'])
def UserAll():
    users = user_services.lista_usuario()
    return jsonify(users_schema.dump(users)), 200

# metodo protegido por los servicios de admin
@user_api.route('/<int:id_user>' ,methods=['GET'])
def user_by_id(id_user):
    findUser = user_services.buscar_usuario(id_user)
    if not findUser:
        return jsonify({'message': "usuario no encontrado"}), 401
    return jsonify(user_schema.dump(findUser)), 200

# seccion de prototipo para la busqueda de usuarios por su nombre
@user_api.route('/username/<name_users>', methods=['GET'])
def user_by_name(name_users):
    usuarios = user_services.lista_usuario_by_name(name_users)
    if not usuarios:
        return jsonify({'menssage': f"No hay usuarios con el nombre de {name_users}"})
    return jsonify(users_schema.dump(usuarios)), 200

# UREGENTE: convertir esta zona en la parte del login implementar los metodos GET y POST
@user_api.route('/' ,methods=['POST'])
def create_user():
    # verificacion de la estructura de datos (mira si todo se encuentra en su citio)
    data = request.get_json()
    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400 # encontrar una forma de clasificar errores
    
    if _comprobate(password=data['password'], email=data['email']):
        return jsonify({'message': "Faltan atributos por ingresar "}), 400
    
    if _comprobarExistencia(email=data['email']):
        return jsonify({'message' : "Error, ya existe una cuenta con el email"}), 400
    
    new_user = user_services.agregar_usuario(data)
    return jsonify(user_schema.dump(new_user)), 201

# UREGENTE: convertir esta zona en la parte del login implementar los metodos GET y POST
# @user_api.route('')
# def login_user():
#     pass

# metodo de modificacion para el usuario (tendrá una referencia automatica al iniciar seccion)
# @user_api.route()
# def user_my_update_account():
#     pass

# metodo eliminacion para el usuario (tendrá una referencia automatica al iniciar seccion)
# @user_api.route()
# def user_my_delete_account():
#     pass

# metodo protegido por los servicios de admin
@user_api.route('/<int:id_user>' ,methods=['PATCH'])
def upgrade_user(id_user):
    data = request.get_json()
    # permite encontrar al usuario si es que este existe!
    userUpgrade = user_services.buscar_usuario(id_user)
    if not userUpgrade:
        return jsonify({'message': "usuario no encontrado"}), 401
    
    result = user_services.editar_usuario(userUpgrade, data)
    return jsonify(user_schema.dump(result)), 200 # pendiente a este resulatado

# metodo protegido por los servicios de admin
@user_api.route('/<int:id_user>' ,methods=['DELETE'])
def delete_user(id_user):
    # permite encontrar al usuario si es que este existe!
    userDelete = user_services.buscar_usuario(id_user)
    if not userDelete:
        return jsonify({'message': "usuario no encontrado"}), 401
    
    subdata = user_services.eliminar_usuario(userDelete)
    return jsonify(subdata), 200

# metodos privados y funcionales para este controlador
def _comprobarExistencia(email):
    # si es true entonces existe, si esta vacio entonces no
    return user_services.comprobate_email_real(email)

# es opcional en esta parte
def _comprobate(password, email):
    return True if(not password or not email) else False