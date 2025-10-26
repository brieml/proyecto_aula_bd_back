from flask import Blueprint, request, jsonify
from app.services.ServicesBase import GroupServicesMain
from app.schemas.Schemas import group_schema, groups_schema

#preparar instancias de los servicios y entidades correspondientes del schemas
#crear una instancia de las rutas que corresponde a cada unidad
group_api = Blueprint('group_user', __name__)
grupoServices = GroupServicesMain()

# puede que este metodo no este protegido, puede que aparezca en la lista de grupos por defecto (hay que poner su el grupo es privado y eso)
# retorna una lista de grupos 
@group_api.route('/', methods=['GET'])
def groupAll():
    grupos = grupoServices.lista_grupos()
    return jsonify(groups_schema.dump(grupos))

# permite encontrar una lista de nombre de grupos parecidos a la busqueda
# @group_api.route()
# def find_group_by_name():
#     pass

@group_api.route('/<int:id_group>', methods=['GET'])
def group_by_id(id_group):
    grupo = grupoServices.obtener_grupo_id(id_group)
    if not grupo:
        return jsonify({'message': f"No se ha encontrado el grupo con la id {id_group}"})
    return jsonify(group_schema.dump(grupo)), 201

@group_api.route('/',methods=['POST'])
def createGroup():
    data = request.get_json()
    errors = group_schema.validate(data)
    if errors:
        return jsonify(errors), 404 # encontrar una forma de clasificar errores
    grupo = grupoServices.agregar_grupo(data)
    return jsonify(group_schema.dump(grupo)), 200



@group_api.route('/<int:id_group>',methods=['PATCH'])
def updategroup(id_group):
    data = request.get_json()
    oldgrupo = grupoServices.obtener_grupo_id(id_group)
    if not oldgrupo:
        return jsonify({'message': f"No se ha encontrado el grupo con la id {id_group}"}), 404
    newgrupo = grupoServices.editar_grupo(oldgrupo, data)
    return jsonify(group_schema.dump(newgrupo)), 201

@group_api.route('/<int:id_group>',methods=['DELETE'])
def deleteGroup(id_group):
    grupo = grupoServices.obtener_grupo_id(id_group)
    if not grupo:
        return jsonify({'message': f"No se ha encontrado el grupo con la id {id_group}"}), 404
    action_delete = grupoServices.eliminar_grupo(grupo)
    return jsonify(action_delete), 201
