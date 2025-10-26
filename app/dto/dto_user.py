#
# clase encargada de pasar solo los datos necesarios de los usuarios
# #

class DTOUser():
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def getNameUserDTO(self):
        return self.name
    
    def getEmailUserDTO(self):
        return self.email
    
    def getPasswordUserDTO(self):
        return self.password