from abc import ABC, abstractmethod

#
# clase abstracta dedicada a la implementacion de metodos del tipo 
# interfaz, con la intencio de dejar la redundancia
# #
class repositoryAbstractGeneric(ABC):
    # methods abstract for the conventional CRUD

    # method allows find all the objects generics
    @abstractmethod
    def get_all(self):
        pass

    # method allows find the object by number id (data type: integer)  
    @abstractmethod
    def get_by_id(self, id_object:int):
        pass
    
    # method 
    @abstractmethod
    def create_object(self):
        pass

    #
    @abstractmethod
    def update_object(self):
        pass
    
    #
    @abstractmethod
    def delete_object(self):
        pass