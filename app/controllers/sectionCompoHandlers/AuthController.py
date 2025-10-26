
# implementar la logica de redireccion a los controladores crear_cuenta e ingresar_cuenta 
# alojar logica a los demas metodos


from flask import Blueprint, request, render_template, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
# from werkzeug.security import is_safe_url
from urllib.parse import urlparse 
from app.schemas.Schemas import perfil_schema
from app.services.auth.authservices import LoginServicesMain
from app.services.ServicesBase import UserServicesMain

auth_api = Blueprint('auth', __name__)
user_services = UserServicesMain()
auth_services = LoginServicesMain()

# Componentes Base de los controladores de Auth

# ATENCION: por medio de este 
# por medio de este metodo podemos encontrar el perfil que se mantiene ligado al usuario 
@auth_api.route('/register', methods=['GET', 'POST'])
def crear_cuenta():
    try:
        datos = request.get_json()
        if _comprobate(password=datos['password'], email=datos['email']):
            return jsonify({'message': "Error, falta llenar el email o contraseña"}), 400

        if _comprobarExistencia(email=datos['email']):
            return jsonify({'message': "Error, ya existe una cuenta con ese correo"}), 400

        # permite registrar al usuario a la base de datos
        # new_perfil = auth_services.register_user(data_all=datos)
        cuenta_perfil = auth_services.register_user(data_all=datos) # se usa solo si requiere redireccion o acceso al login 

        if cuenta_perfil['bool']:
            return redirect(url_for('dashboard.view_index_dashboard')), 200
        
        return jsonify(cuenta_perfil), 400

        # next_view = request.args.get('next_view')
        # # las siguientes funciones a continucacion hacen parte de la logica de rutas (instancia y seguridad de las mismas)
        # _is_save = True
        # if next_view:
        #     rootHost = urlparse(next_view)
        #     if rootHost.netloc and rootHost.netloc != request.host_url:
        #         _is_save = False

        # # si la url ingresada existe y a su vez es segura (pertenece al proyecto) puede redirigirse a esa vista
        # if next_view and _is_save:
        #     return redirect(next_view)
        # ruta de redireccion por defecto (si es que la ruta a encontrar es insegura)
        # return jsonify(perfil_schema.dump(new_perfil)), 201 # debug para encontrar el usuario que tiene relacion con el perfil
        # return jsonify(access_token=new_perfil)
    except Exception as error:
        return jsonify({
            'message': "error al crear un usuario",
            'error': f"causa {error}"
        }), 401

# una forma de confirmar de que dicho usuario existe
@auth_api.route('/login_user', methods=['GET', 'POST'])
def ingresar_cuenta():
    try:
        #(esta parte solo si el usuario mantiene una seccion lo redirige a la parte principal del dashboard)
        if current_user.is_authenticated:
            return render_template(url_for('dashboard.view_index_dashboard')) # <-- aqui poner otra plantilla  

        datos = request.get_json()
        if _comprobate(password=datos['password'], email=datos['email']):
            return jsonify({'message': "Error, falta llenar el email o contraseña"}), 400
        # por ahora permite retornar el usuario que se encuentra en la base de datos
        cuenta_perfil = auth_services.authenticate_user(dateuser=datos)

        if cuenta_perfil['bool']:
            return redirect(url_for('dashboard.view_index_dashboard')), 200
        
        return jsonify(cuenta_perfil), 400
        # if not cuenta_perfil:
        #     return {'message': "password o email incorrectos"} # un error presente en el login
        # next_view = request.args.get('next_view')
        # _is_save = True
        # if next_view:
        #     rootHost = urlparse(next_view)
        #     if rootHost.netloc and rootHost.netloc != request.host_url:
        #         _is_save = False

        # # si la url ingresada existe y a su vez es segura (pertenece al proyecto) puede redirigirse a esa vista
        # if next_view and _is_save:
        #     return redirect(next_view)
        
        # return jsonify(access_token=cuenta_perfil), 200 # debug para encontrar el usuario que 
    except Exception as error:
        return jsonify({
            'message': "error al entrar ingresar con la cuenta",
            'error': f"causa {error}"
        }), 401


# metodo encargado de cerrar la seccion del usuario (en este caso tiene que redirigirlo a una vista en especifico)
# aqui se puede controlar las redirecciones a x seccion con respecto a dicha accion (en este caso el usuario finaliza su seccion)

@auth_api.route('/profile')
@login_required # <-- será despresiado
def data_perfil():
    # esta parte lo que hace es llevar los datos de perfil por medio de la entidad user a la siguiente direccion
    # en este caso una relacionada con el perfil (en este caso la recomendacion es usar jinja 2) 
    perfil_cache = current_user.perfil
    return render_template('perfil/vista.html', perfil=perfil_cache)

# metodos privados y funcionales para este controlador
def _comprobarExistencia(email):
    # si es true entonces existe, si esta vacio entonces no
    return user_services.comprobate_email_real(email)

# es opcional en esta parte
def _comprobate(password, email):
    return True if(not password or not email) else False

# aqui se guardan las instancias del la estructura funcional URL_HOST
def _comprobarUrlHost():
    pass

