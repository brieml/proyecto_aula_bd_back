
#
# Clase encargada de controlar los errores registrados en los modulos implicados <sera refactorizada>
# 
class MCE(Exception):
    def __init__(self, messageGeneric = "Error generico registrado"):
        self.message = messageGeneric
        super().__init__(self.message)