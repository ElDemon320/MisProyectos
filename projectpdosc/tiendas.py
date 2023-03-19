import csv  # Librería para abrir, leer y escribir archivos CSV
from csv import writer  # Importa el módulo "writer" de la librería "csv"# Importa el módulo "writer" de la librería "csv"

class Tiendas:  # Clase Tiendas

    def __init__(self): # Constructor de la clase Tiendas
        pass # Inicializa el objeto de la clase Tiendas

    def listarTiendas(self) -> bool: # Metodo para listar las tiendas registrados
        print("Listado de Tiendas") # Imprime en pantalla el mensaje
        try: # Prueba el código y si ocurre una excepción la atrapa
            with open("tiendas.csv", "r") as file: # Abre el archivo para tener acceso a los registros
                reader = csv.DictReader(file, delimiter=",") # Crea un objeto reader para leer los registros separándolos por el delimitador ,
                for row in reader: # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
                    print(f"Registro: {row}") # Imprime los datos del registro como un diccionario
            return True # Regresa True si el método se ejecutó correctamente
        except Exception as e: # Atrapa cualquier excepción
            print(f"Error listarTiendas() :{e.args}") # Muestra en consola el error que ocurrió
            return False # Regresa False si ocurrió un error en el método
    
    def insertarTienda(self) -> bool: # Metodo para insertar una tienda
        print("Función insertarTienda()")  # Imprime el mensaje "Método insertarProducto" para verificar que se esté invocando al método de forma correcta.
        
        no = input("Numero: ")  # Pide al usuario que introduzca el no de la tienda
        nombre = input("Nombre: ")  # Pide al usuario que introduzca el nombre del tienda
        longitud = input("Longitud: ")  # Pide al usuario que introduzca la longitud de la tienda
        latitud = input("Latitud: ") # Pide al usuario que introduzca la latitud de la tienda
        direccion = input("Direccion: ") # Pide al usuario que introduzca la direccion de la tienda

        try: # Prueba el código y si ocurre una excepción la atrapa
            fila_tiendas = [no, nombre, longitud, latitud, direccion]  # Crea una lista con los valores de las variables sku, nombre y unidad.

            print(f"INSERTAR: Numero: {no}; Nombre: {nombre}; Longitud: {longitud}; Latitud: {latitud}; Direccion: {direccion}")

            with open('tiendas.csv', 'a') as objetoArchivo:  # Abre el archivo "tiendas.csv" en "append mode" para poder agregar una fila al documento, 
            #                                                    y crea un objeto de este documento para poder trabajarlo. Se guarda como "objetoArchivo".

                objeto_w = writer(objetoArchivo)  # Se consigue un objeto con la función writer() a partir de "objetoArchivo". Se guarda como "objeto_w"
                objeto_w.writerow(fila_tiendas)  # Se utiliza la lista "fila_tiendas" como argumento para añadir la nueva fila, haciendo uso de la función writerow()

                objetoArchivo.close()  # Se cierra el objeto del documento "objetoArchivo" con la función close().
            return True # Regresa True si el método se ejecutó correctamente
        except Exception as e: # Atrapa cualquier excepción
            print(f"Error insertarTienda(): {e.args}") # Muestra en consola el error que ocurrió
            return False # Regresa False si ocurrio un error en el metodo
    
    def actualizarTienda(self, no: str, nombre: str, longitud: str, latitud: str, direccion: str) -> bool: #Metodo para actualizar tienda
        print("Método actualizarTienda()") # Imprime un mensaje en la consola
        try: # Intenta ejecutar el bloque de código que sigue
            with open("tiendas.csv", "r") as file: # Abre el archivo tiendas.csv en modo de lectura y lo asigna a la variable file
                reader = csv.reader(file) # Crea un objeto reader para leer el contenido del archivo
                tiendas = list(reader) # Convierte el objeto reader en una lista de tiendas
            for tienda in tiendas: # Recorre cada tienda en la lista de tiendas
                if tienda[0] == no: # Si el número de la tienda coincide con el número de tienda que se quiere actualizar
                    tienda[1] = nombre # actualiza el nombre de la tienda
                    tienda[2] = longitud # actualiza la longitud de la tienda.
                    tienda[3] = latitud # actualiza la latitud de la tienda
                    tienda[4] = direccion # actualiza la dirección de la tienda
            with open("tiendas.csv", "w", newline="") as file: # Abre el archivo tiendas.csv en modo de escritura y lo asigna a la variable file
                writer = csv.writer(file) # Crea un objeto writer para escribir en el archivo
                writer.writerows(tiendas) # Escribe la lista actualizada de tiendas en el archivo
            print(f"Tienda con numero '{no}' actualizado exitosamente.") # Imprime un mensaje en la consola indicando que la tienda ha sido actualizada con éxito
            return True # Devuelve True para indicar que la actualización fue exitosa
        except Exception as e: # Si ocurre un error durante la ejecución del bloque de código, se ejecuta este bloque
            print(f"Error actualizarTienda(): {e.args}") # Imprime un mensaje en la consola indicando el tipo de error que ha ocurrido
            return False # Devuelve False para indicar que la actualización no fue exitosa

    def buscarTienda(self) -> bool: # Método para buscar una tienda
        print("Buscar Tienda") # Imprime el mensaje "Buscar Tienda" para verificar que se esté invocando al método de forma correcta.
        try: # Prueba el código y si ocurre una excepción la atrapa
            with open("tiendas.csv", "r") as file: # Abre el archivo csv en modo "read" para leer el contenido del archivo
                reader = csv.reader(file, delimiter=",") # Crea un objeto reader para leer los registros separados por el delimitador ","
                nombre = input("Ingrese el numero de la tienda a buscar: ") # Pide al usuario ingresar el nombre del tienda a buscar
                for row in reader: # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
                    if row[0] == nombre: # Si el primer elemento de la fila coincide con el nombre ingresado por el usuario
                        print(f"Registro encontrado: {row}") # Muestra en consola los datos del registro encontrado
                        return True # Regresa True si el registro se encontró correctamente
                print("No se encontró ningún registro con el nombre ingresado") # Muestra un mensaje en consola indicando que no se encontró ningún registro con el nombre ingresado por el usuario
                return False # Regresa False si no se encontró ningún registro con el nombre ingresado por el usuario
        except Exception as e: # Atrapa cualquier excepción
            print(f"Error buscarTienda(): {e.args}") # Muestra en consola el error que ocurrió
            return False # Regresa False si ocurrió un error en el método
    
    def borrarTienda(self) -> bool: #Metodo para borrar una tienda
        print("Borrar Tienda") #Imprime para que se note que se esta llamando al metodo borrarTienda()
        no = input("Ingrese el numero de la tienda que desea borrar: ") # Pide al usuario el no del tienda que desea borrar
        try: # Prueba el código y si ocurre una excepción la atrapa
            with open("tiendas.csv", "r") as file: # Abre el archivo para tener acceso a los registros
                reader = csv.reader(file, delimiter=",") # Crea un objeto reader para leer los registros separándolos por el delimitador ,
                rows = list(reader) # Convierte los registros a una lista de filas
            with open("tiendas.csv", "w", newline="") as file: # Abre el archivo en modo "w" para escribir los registros
                writer = csv.writer(file, delimiter=",") # Crea un objeto writer para escribir los registros separándolos por el delimitador ,
                for row in rows: # Recorre todas las filas encontradas
                    if row[0] == no: # Si el no de la fila es igual al no del tienda a borrar, no escribe la fila en el archivo
                        print(f"Tienda '{row[1]}' borrado exitosamente.") # Imprime un mensaje indicando que el tienda fue borrado exitosamente
                    else: # Si el no de la fila no es igual al no del tienda a borrar, escribe la fila en el archivo
                        writer.writerow(row)
            return True # Regresa True si el método se ejecutó correctamente
        except Exception as e: # Atrapa cualquier excepción
            print(f"Error borrarTienda(): {e.args}") # Muestra en consola el error que ocurrió
            return False # Regresa False si ocurrió un error en el método
