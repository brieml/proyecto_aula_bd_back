# aqui se define las necesidades principales de la entidad del usuarios 
# definir las sentencias principales de la clase perfil
from werkzeug.security import check_password_hash, generate_password_hash
from app.repository.UserRepository import UserRepo

class UserServicesRestoras():
    def __init__(self):
        self.undergroudUser = UserRepo()

    # sección para usar
    def encriptarClave(self, password_convert:str):
        return generate_password_hash(password_convert)

    # retornara un bool cuando este se cumpla (ya sea falso o verdadero)
    def chequearClave(self, email_user, password_confirmt:str):
        user = self.undergroudUser.get_by_email(email_user)
        # hay que planificar las sentencias de excepción en cada modulo aplicado
        if user is None:
            return {
                'message': "el usuario con email ese email no existe", # <-- una captura con estos datos en el DOM
                'operatiom': False # <-- no creo que sea necesario o si?
            }
        return check_password_hash(password_confirmt, user.email) 