from src.game.Cacho import Cacho


class Jugador:

    def __init__(self, nombre: str, cacho):
        '''
        :param nombre: Nombre del jugador
        :param cacho: Dependency Injection de una instancia de Cacho
        '''

        self.__nombre = nombre
        self.__cacho = cacho

    def get_cantidad_dados(self):
        return len(self.__cacho.getDados())

    def get_cacho(self):
        return self.__cacho

    def set_cacho(self, cacho: Cacho):
        self.__cacho = cacho

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre