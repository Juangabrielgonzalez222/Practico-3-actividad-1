class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.salir
                         }
    def opcion(self,op,manejador):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(manejador)
    def salir(self,manejador):
        print('Usted salio del programa')
    def opcion1(self,manejador):
        id=None
        while id!= -1:
            id = int(input('Ingrese el id del libro o -1 para no realizarlo:'))
            if (manejador.mostrarInformacionLibroConID(id)==-10):
                print('Error: el id ingresado no pertenece a ningun libro.')
            else:
                id=-1
    def opcion2(self,manejador):
        palabra = input('Ingrese una palabra o S para no realizarlo:')
        while(palabra!="S"):
            sinerror=manejador.busquedaPorPalabra(palabra)
            if(sinerror==-10):
                palabra="S"
    def opcion3(self,manejador):
        manejador.test()