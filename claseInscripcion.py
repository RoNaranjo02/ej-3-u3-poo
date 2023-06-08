class Inscripcion:
    __fechaInscripcion = '22/05/2023'
    __pago : bool
    __persona : object
    __taller : object

    def __init__(self, persona, taller):
        self.__pago = False
        self.__persona = persona
        self.__taller = taller

    @classmethod
    def getFechaInscripcion(cls):
        return cls.__fechaInscripcion
    
    def getPago(self):
        return self.__pago
    
    def setPago(self):
        self.__pago = not self.__pago

    def __str__(self):
        cadena = 'Fecha de inscripcion: ' + self.__fechaInscripcion + '\n'
        cadena += str(self.__persona)
        cadena += str(self.__taller)
        return cadena
    
    def mostrarTaller(self):
        print("El taller de la persona ingresada es: {} y debe el monto {}".format(self.__taller.getNombre(), self.__taller.getMonto()))

    def getPersonaDni(self):
        return self.__persona.getDni()
    
    def getId(self):
        return self.__taller.getIdTaller()
    
    def getPersona(self):
        return self.__persona

    def modificarPago(self):
        self.setPago()

        

    