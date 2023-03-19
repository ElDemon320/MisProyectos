from productos import Productos  # Importa la clase Productos desde el módulo productos
from tiendas import Tiendas  # Importa la clase Tiendas desde el módulo tiendas

class Main():  # Define una nueva clase llamada Main
    
    def __init__(self) -> None:  # Define el constructor de la clase
        self.productos = Productos()  # Crea una instancia de la clase Productos y la asigna al atributo productos
        self.tiendas = Tiendas()  # Crea una instancia de la clase Tiendas y la asigna al atributo tiendas

    def menu_principal(self):  # Define la función que muestra el menú principal
        while True:
            print("1. Administrar Productos")  # Muestra la opción para administrar productos
            print("2. Administrar Tiendas")  # Muestra la opción para administrar tiendas
            print("0. Salir")  # Muestra la opción para salir del programa
            opcion = input("Seleccione una opción: ")  # Solicita al usuario que ingrese una opción
            if opcion == "1":  # Si el usuario elige la opción 1
                self.menu_productos()  # Redirige al menú de productos
            elif opcion == "2":  # Si el usuario elige la opción 2
                self.menu_tiendas()  # Redirige al menú de tiendas
            elif opcion == "0":  # Si el usuario elige la opción 0
                break  # Sale del programa
            else:  # Si el usuario ingresa una opción no válida
                print("Opción no válida. Por favor, intente de nuevo.\n")  # Muestra un mensaje de error

    def menu_productos(self):  # Define la función que muestra el menú de productos
        while True:
            print("\n---- Menú de Productos ----")  # Muestra el título del menú de productos
            print("1. Listar productos")  # Muestra la opción para listar los productos
            print("2. Insertar producto")  # Muestra la opción para insertar un nuevo producto
            print("3. Buscar producto por SKU")  # Muestra la opción para buscar un producto por su SKU
            print("4. Actualizar producto")  # Muestra la opción para actualizar un producto existente
            print("5. Borrar producto")  # Muestra la opción para borrar un producto existente
            print("0. Regresar al Menú Principal")  # Muestra la opción para regresar al menú principal
            opcion = input("Seleccione una opción: ")  # Solicita al usuario que ingrese una opción
            if opcion == "1":  # Si el usuario elige la opción 1
                self.productos.listarProductos()  # Llama al método listarProductos de la instancia de la clase Productos
            elif opcion == "2":  # Si el usuario elige la opción 2
                self.productos.insertarProducto()  # Llama al método insertarProducto de la instancia de la clase Productos
            elif opcion == "3":  # Si el usuario elige la opción 3
                self.productos.buscarProducto()  # Llama al método buscarProducto de la instancia de la clase Productos
            elif opcion == "4": # Si el usuario elige la opción 4
                sku = input("Ingrese el SKU del producto a actualizar: ")  #Pide al usuario el nuevo sku del producto
                nombre = input("Ingrese el nuevo nombre del producto: ") # Pide al usuario el nuevo nombre del producto
                unidad = input("Ingrese la nueva unidad del producto: ") # Pide al usuario la nueva unidad del producto
                print("Llamar metodo actualizarProducto()") # Imprime esta linea si entro al metodo
                self.productos.actualizarProducto(sku, nombre, unidad) # Llama al método actualizarProductos de la instancia de la clase Productos
            elif opcion == "5": #Si el usuario elige la opcion 5
                self.productos.borrarProducto() # Llama al método borrarProductos de la instancia de la clase Productos
            elif opcion == "0": #Si el usuario elige la opcion 0
                break # Sale del ciclo while
            else: #Si la opcion seleccionada no es valida
                print("Opción no válida. Por favor, intente de nuevo.\n") #Imprime este mensaje indicando que la opcion no fue valida

    # Función que muestra el menú de tiendas
    def menu_tiendas(self):
	    while True:  # Inicia un ciclo while infinito
	        print("\n---- Menú de Tiendas ----")  # Imprime el título del menú de tiendas
	        print("1. Listar tiendas")  # Imprime la opción 1 del menú de tiendas
	        print("2. Insertar tienda")  # Imprime la opción 2 del menú de tiendas
	        print("3. Buscar tienda por número")  # Imprime la opción 3 del menú de tiendas
	        print("4. Actualizar tienda")  # Imprime la opción 4 del menú de tiendas
	        print("5. Borrar tienda")  # Imprime la opción 5 del menú de tiendas
	        print("0. Regresar al Menú Principal")  # Imprime la opción 0 del menú de tiendas
	        opcion = input("Seleccione una opción: ")  # Solicita al usuario que seleccione una opción del menú
	
	        if opcion == "1":  # Si la opción seleccionada es 1
	            self.tiendas.listarTiendas()  # Llama al método listarTiendas de la instancia de Tiendas
	        elif opcion == "2":  # Si la opción seleccionada es 2
	            self.tiendas.insertarTienda()  # Llama al método insertarTienda de la instancia de Tiendas
	        elif opcion == "3":  # Si la opción seleccionada es 3
	            self.tiendas.buscarTienda()  # Llama al método buscarTienda de la instancia de Tiendas
	        elif opcion == "4":  # Si la opción seleccionada es 4
	            no = input("Ingrese el no del tienda a actualizar: ")  # Solicita al usuario que ingrese el número de la tienda a actualizar
	            nombre = input("Ingrese el nuevo nombre del tienda: ")  # Solicita al usuario que ingrese el nuevo nombre de la tienda
	            longitud = input("Ingrese la nueva longitud del tienda: ")  # Solicita al usuario que ingrese la nueva longitud de la tienda
	            latitud = input("Ingrese la nueva latitud del tienda: ")  # Solicita al usuario que ingrese la nueva latitud de la tienda
	            direccion = input("Ingrese la nueva direccion del tienda: ")  # Solicita al usuario que ingrese la nueva dirección de la tienda
	            self.tiendas.actualizarTienda(no, nombre, longitud, latitud, direccion)  # Llama al método actualizarTienda de la instancia de Tiendas
	            print("Llamar metodo actualizarTiendas()")  # Imprime un mensaje indicando que se debe llamar al método actualizarTiendas
	        elif opcion == "5":  # Si la opción seleccionada es 5
	            self.tiendas.borrarTienda()  # Llama al método borrarTienda de la instancia de Tiendas
	        elif opcion == "0":  # Si la opción seleccionada es 0
	            break  # Sale del ciclo while
	        else:  # Si la opción seleccionada no es válida
	            print("Opción no válida. Por favor, intente de nuevo.\n")  # Imprime un mensaje indicando que la opción seleccionada no es válida y se debe intentar de nuevo

if __name__ == "__main__": # Esta línea verifica si este archivo está siendo ejecutado como el archivo principal (en lugar de ser importado por otro archivo. Si es así, entonces ejecutará lo que se encuentra debajo
    main = Main() # Crea un objeto de la clase Main y lo almacena en la variable 'main'
    main.menu_principal() # Llama al método 'menu_principal' del objeto 'main'
