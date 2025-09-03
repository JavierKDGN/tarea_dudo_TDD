from src.game.Cacho import Cacho


class Jugador:

    def __init__(self, nombre: str, cacho):
        '''
        :param nombre: Nombre del jugador
        :param cacho: Dependency Injection de una instancia de Cacho
        '''

        self.__nombre = nombre
        self.__cacho = cacho

    def getCantidadDados(self):
        return len(self.__cacho.getDados())

    def getCacho(self):
        return self.__cacho

    def setCacho(self, cacho: Cacho):
        self.__cacho = cacho

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre