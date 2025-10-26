from flask import Blueprint, request, jsonify
#preparar instancias de los servicios y entidades correspondientes del schemas

#crear una instancia de las rutas que corresponde a cada unidad
admin_api_users = Blueprint('admin_user', __name__)

@admin_api_users.route('/<int:id_user>', methods=['DELETE'])
def get_user_by_id(id_user):
    pass

@admin_api_users.route('/', methods=['DELETE'])
def get_all_user():
    pass

@admin_api_users.route('/<int:id_user>', methods=['DELETE'])
def delete_user(id_user):
    pass

