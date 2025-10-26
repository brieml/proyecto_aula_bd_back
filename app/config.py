import os
from dotenv import load_dotenv
from datetime import timedelta

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class Config:
    """Configuración base."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_KEY_SECRET = os.environ.get('JWT_KEY_SECRET')
    JWT_LEEWAY = 10
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1) # El token de acceso dura 1 hora
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30) # El token de refresco dura 30 días
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    TESTING = True

class DevelopmentConfig(Config):
    """Configuración de desarrollo."""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG = True

class TestingConfig(Config):
    """Configuración de testing."""
    TESTING = True
    # Usar una base de datos en memoria para las pruebas
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


config = {
    'real': Config,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}