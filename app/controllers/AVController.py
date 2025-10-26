from flask import Blueprint, request, jsonify

# definir las ruta completas de estos endpoints
AV_api = Blueprint('agent_virtual', __name__)

@AV_api.route('', methods=['GET'])
def AVAll(self):
    pass

@AV_api.route('/avs/<int:id_av>', methods=['GET'])
def AV_get_id(id_av):
    pass

@AV_api.route('/avs/<int:id_av>', methods=['POST'])
def AV_create():
    pass

@AV_api.route('/avs/<int:id_av>', methods=['PATCH'])
def AV_update(id_av):
    pass

@AV_api.route('/avs/<int:id_av>', methods=['DELETE'])
def AV_delete(id_av):
    pass