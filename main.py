from menu import menuOpciones
from claseTallerCapacitacion import TallerCapacitacion

if __name__ == "__main__":
    taller = TallerCapacitacion()
    taller.cargarTalleres()
    menu = menuOpciones()
    menu.opciones(taller)