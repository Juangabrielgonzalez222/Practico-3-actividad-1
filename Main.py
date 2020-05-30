from Clase_menu import Menu
from Clase_manejador import ManejadorLibros
if __name__=='__main__':
    op=None
    menu=Menu()
    manejador=ManejadorLibros()
    errores=manejador.cargarLibros()
    if errores !=100:    
        while(op!=4):
            print("Menu:")
            print("Ingrese 1 para buscar un libro por id y ver información relacionada a el mismo")
            print("Ingrese 2 para buscar por palabra un libro o capitulo del mismo ")
            print("Ingrese 3 para ejecutar test")
            print("INgrese 4 para salir")
            op=int(input("Ingrese opción:"))
            menu.opcion(op,manejador)
    else:
        print("Se finalizo la ejecución debido a un error en el archivo")
        
    
    
    

