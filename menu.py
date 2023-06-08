class menuOpciones():
    __opcion : int
    
    def __init__(self):
        self.__opcion = 0

    def opciones(self,taller):
        while self.__opcion != 6:
            print("||---Menu de Opciones---||")
            print("1) Inscribir una persona en un taller")
            print("2) Consultar inscripcion ")
            print("3) Consultar inscriptos a un taller")
            print("4) Registrar pago ")
            print("5) Guardar inscripciones ")
            print("6) Salir")
            self.__opcion = int(input("Seleccione una opcion: "))

            if self.__opcion == 1:
                taller.inscribirPersona()

            elif self.__opcion == 2:
                ingdni = str(input("Ingrese el dni de una persona "))
                taller.consultarInscripcion(ingdni)

            elif self.__opcion == 3:
                ingtaller = int(input("Ingrese el identificador de un taller "))
                taller.consultarInscripciones(ingtaller)

            elif self.__opcion == 4:
                ingdni = str(input("Ingrese el dni de una persona "))
                taller.registrarPago(ingdni)

            elif self.__opcion == 5:
                taller.guardarInscripciones()

            elif self.__opcion == 6:
                print("FIN")

            else: 
                print("Opcion invalida, vuelva a ingresar una opcion.")
