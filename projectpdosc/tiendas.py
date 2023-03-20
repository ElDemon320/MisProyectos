import csv  # Librería para abrir, leer y escribir archivos CSV
from csv import reader, writer  # Importa el módulo "reader" y "writer" de la librería "csv"

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
    
    def insertarTienda(self) -> bool:  # Método para insertar un tienda
        print("Función insertarTienda()") #Imprime si si esta llamando a la funcion insertarTienda()
        numero = input("Numero: ")  # Pide al usuario que introduzca el numero de la tienda
    
        try: # Verifica si la tienda ya existe en el archivo tiendas.csv
            with open('tiendas.csv', 'r') as archivo:  # Abre el archivo tiendas.csv en modo lectura
                lector = reader(archivo)  # Crea un objeto lector para leer el archivo
                for fila in lector:  # Itera sobre todas las filas del archivo
                    if fila[0] == numero:  # Si el numero de la tienda ya existe en el archivo
                        print("La tienda con ese numero ya existe.") # Da un mensaje al usuario de que la tienda con ese numero ya existe
                        archivo.close()  # Cierra el archivo
                        return False  # Devuelve False indicando que el tienda no se pudo insertar
                archivo.close()  # Cierra el archivo
                # Si la tienda no existe, pide al usuario que introduzca el nombre, longitud, latitud, direccion de la tienda
                nombre = input("Nombre: ")  # Pide al usuario que introduzca el nombre del tienda
                longitud = input("Longitud: ")  # Pide al usuario que introduzca el tipo de longitud del tienda
                latitud = input("Latitud: ")  # Pide al usuario que introduzca la latitud de la tienda
                direccion = input("Direccion: ") # Pide al usuario que introduzca la direccion de la tienda
                # Agrega el nuevo tienda al archivo tiendas.csv
                fila_tiendas = [numero, nombre, longitud, latitud, direccion]  # Crea una lista con los valores de las variables numero, nombre y longitud.
                print(f"INSERTAR: numero: {numero}, Nombre: {nombre}, Longitud: {longitud}, Latitud: {latitud}, Direccion: {direccion}") # Da un mensaje al usuario con los valores que se insertaron
                with open('tiendas.csv', 'a') as objetoArchivo:  # Abre el archivo tiendas.csv en modo escritura y lo deja abierto
                    objeto_w = writer(objetoArchivo)  # Crea un objeto escritor para escribir en el archivo
                    objeto_w.writerow(fila_tiendas)  # Escribe la lista fila_tiendas en el archivo
                    objetoArchivo.close()  # Cierra el archivo
                return True  # Devuelve True indicando que el tienda se insertó correctamente  
        except Exception as e:  # Captura cualquier excepción que ocurra durante la ejecución del código
            print(f"Error insertarTienda(): {e.args}")  # Muestra un mensaje de error
            return False  # Devuelve False indicando que el tienda no se pudo

    
    def actualizarTienda(self) -> bool:  # Define la función actualizarTienda
        print("Función actualizarTienda()")  # Imprime un mensaje en la consola
    
        numero = input("Numero de la tienda a actualizar: ")  # Pide al usuario el Numero de la tienda a actualizar
    
        try:  # Inicia un bloque try-except para manejar excepciones
            
            with open('tiendas.csv', 'r') as archivo: # Abre el archivo 'tiendas.csv' en modo lectura
                lector = reader(archivo) # Crea un objeto que puede leer las filas del archivo "tiendas.csv"
                encontrado = False  # Inicializa una variable booleana para saber si se encontró la tiendacon el numero dado
                for fila in lector: # Itera sobre todas las filas del archivo CSV usando el lector
                    if fila[0] == numero:  # Si el numero de la fila actual coincide con el numero dado por el usuario
                        encontrado = True  # Marca que se encontró e la tienda
                        break  # Sale del ciclo for
                if not encontrado:  # Si no se encontró e la tienda
                    print(f"La tienda con numero '{numero}' no existe.")  # Imprime un mensaje en la consola
                    return False  # Retorna False, indicando que no se pudo actualizar e la tienda
    
            # Si se encontró la tienda
            nombre = input("Nuevo nombre de la tienda: ") # Pide al usuario que ingrese el nuevo nombre de la tienda
            longitud = input("Nueva longitud de la tienda: ") # Pide al usuario que ingrese la nueva longitud de la tienda
            latitud = input("Nueva latitud de la tienda: ") # Pide al usuario que ingrese la nueva latitud de la tienda
            direccion = input("Nueva direccion de la tienda: ") # Pide al usuario que ingrese la nueva longitud de la tienda
            
            with open('tiendas.csv', 'r') as archivo: # Abre el archivo 'tiendas.csv' en modo lectura
                lector = reader(archivo) # Crea un objeto que puede leer las filas del archivo "tiendas.csv"
                filas = list(lector)  # Convierte las filas del archivo CSV en una lista de listas
    
            
            with open('tiendas.csv', 'w', newline='') as archivo: # Abre el archivo 'tiendas.csv' en modo escritura
                escritor = writer(archivo)  # Crea un objeto que puede leer las filas del archivo "tiendas.csv"
                for fila in filas: # Itera sobre todas las filas de la lista de listas
                    if fila[0] == numero:  # Si el numero de la fila actual coincide con el numero dado por el usuario
                        fila[1] = nombre  # Actualiza el nombre de la tienda
                        fila[2] = longitud  # Actualiza la longitud de la tienda
                        fila[3] = latitud # Actualiza la latitud de la tienda
                        fila[4] = direccion # Actualiza la direccion de la tiend
                    escritor.writerow(fila)  # Escribe la fila actual en el archivo CSV
            print(f"La tienda con numero '{numero}' ha sido actualizado exitosamente.")  # Imprime un mensaje en la consola
            return True  # Retorna True, indicando que se pudo actualizar e la tienda

        except Exception as e:  # Si ocurre alguna excepción durante la ejecución del código en el bloque try
            print(f"Error actualizarTienda(): {e.args}")  # Imprime un mensaje de error en la consola
            return False  # Retorna False, indicando que no se pudo actualizar e la tienda

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
    
    def borrarTienda(self) -> bool:
        print("Borrar Tienda") # Imprime un mensaje para indicar que se está llamando al método borrarTienda()
        numero = input("Ingrese el número de la tienda que desea borrar: ") # Pide al usuario el número de la tienda que desea borrar y lo almacena en la variable 'no'
        try: # Inicia un bloque try-except para capturar cualquier excepción que pueda ocurrir en el código
            with open("tiendas.csv", "r") as file: # Abre el archivo 'tiendas.csv' en modo de lectura
                reader = csv.reader(file, delimiter=",") # Crea un objeto reader para leer los registros del archivo, separándolos por el delimitador ","
                rows = list(reader) # Convierte los registros a una lista de filas y los almacena en la variable 'rows'
            with open("tiendas.csv", "w", newline="") as file: # Abre el archivo 'tiendas.csv' en modo de escritura, creando un archivo nuevo si no existe
                writer = csv.writer(file, delimiter=",") # Crea un objeto writer para escribir los registros en el archivo, separándolos por el delimitador ","
                tienda_borrada = False # Crea una variable booleana 'tienda_borrada' inicialmente en False para indicar si se encontró y borró la tienda
                for row in rows: # Recorre todas las filas en la lista 'rows'
                    if row[0] == numero: # Si el número de la fila es igual al número de la tienda que se quiere borrar
                        print(f"Tienda '{row[1]}' borrada exitosamente.") # Imprime un mensaje indicando que la tienda ha sido borrada
                        tienda_borrada = True # Cambia el valor de 'tienda_borrada' a True para indicar que la tienda ha sido borrada
                    else: # Si el número de la fila no es igual al número de la tienda que se quiere borrar
                        writer.writerow(row) # Escribe la fila en el archivo
                if not tienda_borrada: # Si la variable 'tienda_borrada' sigue siendo False, significa que la tienda no ha sido borrada porque no existe en el archivo
                    print(f"La tienda con número '{numero}' no existe.")
            return True # Devuelve True si el método se ha ejecutado correctamente
        except Exception as e: # Si ocurre una excepción, se captura y se almacena en la variable 'e'
            print(f"Error borrarTienda(): {e.args}") # Imprime un mensaje de error con el contenido de la excepción
            return False # Devuelve False si ha ocurrido un error en la ejecución del método
