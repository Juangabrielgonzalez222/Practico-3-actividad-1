import csv
from Clase_libro import Libro
class ManejadorLibros:
    __libros=[]
    def __init__(self):
        self.__libros=[]
    def agregarLibro(self, libro):
        if(type(libro)==Libro):
            self.__libros.append(libro)
            return len(self.__libros)-1
        else:
            print("No se pudo añadir, no era un objeto de la clase Libro")
    def cargarLibros(self):
        archivo=open("libros.csv")
        reader=csv.reader(archivo,delimiter=";")
        posicionLibro=None
        for fila in reader:
            if len(fila)==6:
                posicionLibro=self.agregarLibro(Libro(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]),int(fila[5])))
            elif len(fila)==2:
                self.__libros[posicionLibro].añadirCapitulo(fila[0],int(fila[1]))
            else:
                print("Hay un error en una linea del archivo, no contiene los parametros requeridos, por favor corrija el archivo")
                return -100
    def mostrarInformacionLibroConID(self,id):
        posicion=self.buscarId(id)
        if(posicion !=-1):
            print("Nombre:",self.__libros[posicion].getTitulo(),"Cantidad paginas",self.__libros[posicion].calcularTotalPaginas())
            print("Capitulos:")
            capitulos=self.__libros[posicion].getNombresCapitulos()
            for nombre in capitulos:
                print(nombre)
        else:
            return -10
    def busquedaPorPalabra(self,palabra):
        print("Resultados busqueda de:",palabra)
        for libro in self.__libros:
            bandera=None
            nombrescap=[]
            if(libro.getTitulo().count(palabra)!=0):
                bandera=True
            else:
                nombrescap=libro.getNombresCapitulos()
                for nombre in nombrescap:
                    if(nombre.count(palabra)!=0):
                        bandera=True
            if(bandera):
                print(libro.getTitulo(),"de",libro.getAutor())
        return -10
    def buscarId(self, id):
        i=0
        while(i<len(self.__libros) and self.__libros[i].getIdLibro()!=id):
            i+=1
        if(i>=len(self.__libros)):
            i=-1
        return i
    def test(self):
        manejador2=ManejadorLibros()
        manejador2.cargarLibros()
        print("Test de palabra")
        manejador2.busquedaPorPalabra("Hola")
        manejador2.busquedaPorPalabra("Obj")
        manejador2.busquedaPorPalabra("humano")
        print("Test de id")
        manejador2.mostrarInformacionLibroConID(3)
        manejador2.mostrarInformacionLibroConID(101)