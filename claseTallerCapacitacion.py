from claseInscripcion import Inscripcion
from manejadorPersonas import controlPersonas
from clasePersona import Persona
from manejadorInscripciones import controlInscripciones
import numpy as np
import csv

class TallerCapacitacion:
    __idTaller : int
    __nombre : str
    __vacantes : int
    __montoInsripcion : int
    __dimension : int
    __controlPersonas = controlPersonas()
    __controlInscripciones = controlInscripciones()

    
    def __init__(self, idtaller = 0, nombre = '', vacantes = 0, monto = 0, dimension = 0):
        self.__idTaller = idtaller
        self.__nombre = nombre
        self.__vacantes = vacantes
        self.__montoInsripcion = monto
        self.__dimension = dimension
        self.__talleres = np.empty((dimension), dtype= TallerCapacitacion)

    def setDimension(self, dimension):
        self.__dimension = dimension
        self.__talleres = np.empty((dimension), dtype= TallerCapacitacion)

    def getIdTaller(self):
        return self.__idTaller
    
    def getNombre(self):
        return self.__nombre
    
    def getVacantes(self):
        return self.__vacantes
    
    def getMonto(self):
        return self.__montoInsripcion
    
    def restarVacante(self):
        self.__vacantes -= 1
    

    def cargarTalleres(self):
        archivo = open('Talleres.csv')
        reader = csv.reader(archivo, delimiter = ';')
        cabecera = True
        indice = 0
        for fila in reader:
            if cabecera:
                dimension = int(fila[0])
                self.setDimension(dimension)
                cabecera = False
            else:
                id = int(fila[0])
                nom = str(fila[1])
                vac = int(fila[2])
                mont = int(fila[3])
                instanciaT = TallerCapacitacion(id,nom,vac,mont)
                self.__talleres[indice] = instanciaT
                indice += 1
        archivo.close
        return self.__talleres
    
    def mostrarTalleres(self):
        for i in range(self.__dimension):
            print(self.__talleres[i])


    def inscribirPersona(self):

        self.mostrarTalleres()
        wtaller = int(input("Ingrese el idTaller al que se quiere inscribir: "))
        if self.__talleres[wtaller-1].getVacantes() > 0:
            self.__talleres[wtaller-1].restarVacante()
            persona = self.__controlPersonas.registrarPersona()
            inscribir = Inscripcion(persona, self.__talleres[wtaller-1])
            controlInscripciones.agregarInscripto(self.__controlInscripciones, inscribir)
        else:
            print("No es posible inscribir a la persona")

    def __str__(self):
        return str(self.__idTaller) + ". " + self.__nombre + " "+ str(self.__vacantes) + " " + str(self.__montoInsripcion)

    def consultarInscripcion(self, ingdni):
        band = self.__controlPersonas.buscarPersona(ingdni)
        if band == None:
            print("La persona ingresada no esta inscripta ")
        else:
            self.__controlInscripciones.buscarTaller(ingdni)
        
    def consultarInscripciones(self, ingtaller):
        self.__controlInscripciones.buscarInscripciones(ingtaller)

    def registrarPago(self,ingdni):
        band = self.__controlPersonas.buscarPersona(ingdni)
        if band == None:
            print("La persona ingresada no esta inscripta ")
        else:
            self.__controlInscripciones.registrarElPago(ingdni)

    def guardarInscripciones(self):
        self.__controlInscripciones.guardarDatos()

#testaller = TallerCapacitacion()
#testaller.cargarTalleres()
#testaller.mostrarTalleres()







    
