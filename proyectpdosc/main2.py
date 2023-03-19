from tiendas import Tiendas #Importa la clase Tiendas()
#TODO importar Despensa

class Main2(): # Clase principal

    def __init__(self) -> None: # Constructor de la clase Main
        pass # inicializa el objeto Main

    def menu2(self): # Metodo que muestra el menu del sistema
        tiendas = Tiendas() # Crea un objeto de la clase Prodcutos
        while True: # Bucle infinito para mostrar las opciones del sistema
            print("0.- Listar tiendas") # Opcion para listar los prodcutos
            print("1.- Insertar tienda") # Opcion para insertar un nuevo tienda
            print("2.- Buscar tienda por SKU") # Opcion para buscar tiendas por SKU
            print("3.- Actualizar tienda") # Opcion para actualizar un tienda
            print("4.- Borrar tienda") # Opcion para borrar un tienda
            print("s.- Salir") # Opcion para salir del sistema
            opcion = input("Seleccione una opcion: ") # Solicita al usuario que seleccione una opcion del menu
            if opcion == "0": # Valida si la opcion elegida es el 0
                tiendas.listarTiendas() # Llama al metodo listarTiendass a traves del objeto tiendas
            elif opcion == "1": # Valida si la opcion elegida es el 1
                tiendas.insertarTienda()
                print("Llamar metodo insertarTiendas()")
            elif opcion == "2": # Valida si la opcion elegida es el 2
                tiendas.buscarTienda()
                print("Llamar metodo buscarTiendas()")
            elif opcion == "3": # Valida si la opcion elegida es el 3
                no = input("Ingrese el no del tienda a actualizar: ")
                nombre = input("Ingrese el nuevo nombre del tienda: ")
                longitud = input("Ingrese la nueva longitud del tienda: ")
                latitud = input("Ingrese la nueva latitud del tienda: ")
                direccion = input("Ingrese la nueva direccion del tienda: ")
                tiendas.actualizarTienda(no, nombre, longitud, latitud, direccion)
                print("Llamar metodo actualizarTiendas()")
            elif opcion == "4": # Valida si la opcion elegida es el 4
                tiendas.borrarTienda()
                print("Llamar metodo borrarTiendas()")
            elif opcion == "5": # Valida si la opcion elegida es el 5
                # TODO Programar salir del programa
                print("Salir del programa")

            # TODO rediseñar el menu para agregar los submenus necesarios


if __name__ == "__main__": # Define el modulo principal
    principal = Main2() # Crea un objeto de la clase Main
    principal.menu2() # Llama al metodo menu a traves del objeto principal
