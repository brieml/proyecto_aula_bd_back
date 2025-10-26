from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from .config import config

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
cors = CORS()
login_manager = LoginManager()
jwt = JWTManager()

def create_app(config_name="real"):
    app = Flask(__name__)  # Corregido: Se añade __name__ como import_name

    login_manager.init_app(app)
    app.config.from_object(config[config_name])
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})

    # Definicion de las rutas de las principales entidades
    from .controllers.GrupoController import group_api
    from .controllers.UserController import user_api
    from .controllers.PerfilController import perfil_api
    from .controllers.sectionCompoHandlers.AuthController import auth_api

    app.register_blueprint(group_api, url_prefix='/groups') # futura entidad en ser descartado
    app.register_blueprint(user_api, url_prefix='/users') # futura entidad en ser descartado
    app.register_blueprint(perfil_api, url_prefix='/perfil')
    app.register_blueprint(auth_api, url_prefix='/login') # para register y authentic
    
    # Definicion de las rutas de las principales vistas del proyecto
    from .controllers.sectionCompoHandlers.DashboardController import api_view_dashboard
    
    app.register_blueprint(api_view_dashboard, url_prefix='/dashboard')


    # permite guardar una referencia en cache del usuario e implementarlo en Y acciones de la pagina
    from .repository.UserRepository import UserRepo
    repo_user = UserRepo()
    @login_manager.user_loader
    def load_user(id):
        return repo_user.get_by_id(id)

    return app