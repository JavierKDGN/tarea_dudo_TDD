
class Jugador:

    def __init__(self, nombre: str, cacho):
        '''
        :param nombre: Nombre del jugador
        :param cacho: Dependency Injection de una instancia de Cacho
        '''

        self.nombre = nombre
        self.cacho = cacho

    def get_cantidad_dados(self):
        return self.cacho.contar_dados()