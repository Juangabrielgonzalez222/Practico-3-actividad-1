class Capitulo():
    __titulo=""
    __cantidadPaginas=0
    def __init__(self,titulo,cantidadPaginas):
        self.__titulo=titulo
        self.__cantidadPaginas=cantidadPaginas
    def getTitulo(self):
        return self.__titulo
    def getNumPaginas(self):
        return self.__cantidadPaginas
    