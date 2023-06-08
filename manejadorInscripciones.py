from claseInscripcion import Inscripcion
import csv

class controlInscripciones:
    __listaInscripciones : list

    def __init__(self):
        self.__listaInscripciones = []

    def agregarInscripto(self, inscripto):
        self.__listaInscripciones.append(inscripto)

    def buscarTaller(self, ingdni):
        i = 0
        while i < len(self.__listaInscripciones) and self.__listaInscripciones[i].getPersonaDni() != ingdni:
            i += 1

        if i == len(self.__listaInscripciones):
            return None
        
        else: 
            self.__listaInscripciones[i].mostrarTaller()

    def buscarInscripciones(self, ingtaller):
        for inscripcion in self.__listaInscripciones:
            if inscripcion.getId() == ingtaller:
                print(inscripcion.getPersona())

    def registrarElPago(self, ingdni):
        i = 0
        while i < len(self.__listaInscripciones) and self.__listaInscripciones[i].getPersonaDni() != ingdni:
            i += 1

        if i == len(self.__listaInscripciones):
            return None
        else: 
            self.__listaInscripciones[i].modificarPago()
            print("Se ha registrado el pago. (Pago = {})".format(self.__listaInscripciones[i].getPago()))

    def guardarDatos(self):
        archivo = open('Inscripciones.csv', 'w', newline = '')
        writer = csv.writer(archivo)
        for inscripcion in self.__listaInscripciones:
            dni = inscripcion.getPersonaDni()
            idtaller = inscripcion.getId()
            fecha = inscripcion.getFechaInscripcion()
            pago = inscripcion.getPago()
            newfila = [dni,idtaller,fecha,pago]
            writer.writerow(newfila)
        archivo.close


