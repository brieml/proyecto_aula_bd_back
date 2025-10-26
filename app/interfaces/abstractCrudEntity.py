from abc import ABC, abstractmethod

class ACEdomain(ABC):

    #
    # funcion unica, de acuerdo a las principales funcionalidades
    # y anotaciones de flask, es posible trabajar con un metodo
    # #

    @abstractmethod
    def objectsFuntional(self):
        pass
