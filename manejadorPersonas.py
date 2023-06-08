from clasePersona import Persona

class controlPersonas:
    __listaPersonas : list

    def __init__(self):
        self.__listaPersonas = []

    def registrarPersona(self):
        nom = str(input("Ingrese el nombre de la persona: "))
        dir = str(input("Ingrese la direccion de la persona: "))
        dni = str(input("Ingrese el dni de la persona: "))
        instancia = Persona(nom,dir,dni)
        self.__listaPersonas.append(instancia)
        return instancia
        
    def buscarPersona(self,ingdni):
        i = 0
        while i < len(self.__listaPersonas) and self.__listaPersonas[i].getDni() != ingdni:
            i+=1
        if i == len(self.__listaPersonas):
            i = None
        return i
