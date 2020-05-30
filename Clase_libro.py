from Clase_capitulo import Capitulo
class Libro():
    __idlibro=0
    __titulo=""
    __autor=""
    __editorial=""
    __isbn=0
    __cantidadCapitulos=0
    __capitulos=[]
    def __init__(self,idlibro,titulo,autor,editorial,isbn,cantidadCapitulos):
        self.__idlibro=idlibro
        self.__titulo=titulo
        self.__autor=autor
        self.__editorial=editorial
        self.__isbn=isbn
        self.__cantidadCapitulos=cantidadCapitulos
        self.__capitulos=[]
    def añadirCapitulo(self,titulo,cantidadpag):
            self.__capitulos.append(Capitulo(titulo,cantidadpag))
    def getIdLibro(self):
        return self.__idlibro
    def getTitulo(self):
        return self.__titulo
    def getAutor(self):
        return self.__autor
    def getNombresCapitulos(self):
        nombres=[]
        for capitulo in self.__capitulos:
            nombres.append(capitulo.getTitulo())
        return nombres
    def calcularTotalPaginas(self):
        acumulador=0
        for capitulo in self.__capitulos:
            acumulador+=capitulo.getNumPaginas()
        return acumulador
    def __del__(self):
        for capitulo in self.__capitulos:
            del capitulo
    