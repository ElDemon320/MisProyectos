import csv  # Librería para abrir, leer y escribir archivos CSV
from csv import reader,writer  # Importa el módulo "writer" de la librería "csv"# Importa el módulo "writer" de la librería "csv"


class Productos:  # Clase Productos

  def __init__(self):  # Constructor de la clase Productos
    pass  # Inicializa el objeto de la clase Productos

  def listarProductos(self) -> bool:  # Metodo para listar los productos registrados
    print("Listado de Productos")  # Imprime en pantalla el mensaje
    try:  # Prueba el código y si ocurre una excepción la atrapa
      with open("productos.csv","r") as file:  # Abre el archivo para tener acceso a los registros
        reader = csv.DictReader(file, delimiter=",")  # Crea un objeto reader para leer los registros separándolos por el delimitador ,
        for row in reader:  # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
          print(f"Registro: {row}")  # Imprime los datos del registro como un diccionario
      return True  # Regresa True si el método se ejecutó correctamente
    except Exception as e:  # Atrapa cualquier excepción
      print(f"Error listarProductos() :{e.args}")  # Muestra en consola el error que ocurrió
      return False  # Regresa False si ocurrió un error en el método

  def insertarProducto(self) -> bool:  # Método para insertar un producto
    print("Función insertarProducto()") #Imprime si si esta llamando a la funcion insertarProducto()
    sku = input("SKU: ")  # Pide al usuario que introduzca el SKU del producto

    try: # Verifica si el producto ya existe en el archivo productos.csv
        with open('productos.csv', 'r') as archivo:  # Abre el archivo productos.csv en modo lectura
            lector = reader(archivo)  # Crea un objeto lector para leer el archivo
            for fila in lector:  # Itera sobre todas las filas del archivo
                if fila[0] == sku:  # Si el SKU del producto ya existe en el archivo
                    print("El producto con ese SKU ya existe.") # Da un mensaje al usuario de que el producto con ese SKU ya existe
                    archivo.close()  # Cierra el archivo
                    return False  # Devuelve False indicando que el producto no se pudo insertar
            archivo.close()  # Cierra el archivo
            # Si el producto no existe, pide al usuario que introduzca el nombre y la unidad del producto
            nombre = input("Nombre: ")  # Pide al usuario que introduzca el nombre del producto
            unidad = input("Unidad: ")  # Pide al usuario que introduzca el tipo de unidad del producto
            # Agrega el nuevo producto al archivo productos.csv
            fila_productos = [sku, nombre, unidad]  # Crea una lista con los valores de las variables sku, nombre y unidad.
            print(f"INSERTAR: SKU: {sku}, Nombre: {nombre}, Unidad: {unidad}") # Da un mensaje al usuario con los valores que se insertaron
            with open('productos.csv', 'a') as objetoArchivo:  # Abre el archivo productos.csv en modo escritura y lo deja abierto
                objeto_w = writer(objetoArchivo)  # Crea un objeto escritor para escribir en el archivo
                objeto_w.writerow(fila_productos)  # Escribe la lista fila_productos en el archivo
                objetoArchivo.close()  # Cierra el archivo
            return True  # Devuelve True indicando que el producto se insertó correctamente  
    except Exception as e:  # Captura cualquier excepción que ocurra durante la ejecución del código
        print(f"Error insertarProducto(): {e.args}")  # Muestra un mensaje de error
        return False  # Devuelve False indicando que el producto no se pudo insertar


  def actualizarProducto(self) -> bool:  # Define la función actualizarProducto
    print("Función actualizarProducto()")  # Imprime un mensaje en la consola

    sku = input("SKU del producto a actualizar: ")  # Pide al usuario el SKU del producto a actualizar

    try:  # Inicia un bloque try-except para manejar excepciones
        
        with open('productos.csv', 'r') as archivo: # Abre el archivo 'productos.csv' en modo lectura
            lector = reader(archivo) # Crea un objeto que puede leer las filas del archivo "productos.csv"
            encontrado = False  # Inicializa una variable booleana para saber si se encontró el producto con el SKU dado
            for fila in lector: # Itera sobre todas las filas del archivo CSV usando el lector
                if fila[0] == sku:  # Si el SKU de la fila actual coincide con el SKU dado por el usuario
                    encontrado = True  # Marca que se encontró el producto
                    break  # Sale del ciclo for
            if not encontrado:  # Si no se encontró el producto
                print(f"El producto con SKU '{sku}' no existe.")  # Imprime un mensaje en la consola
                return False  # Retorna False, indicando que no se pudo actualizar el producto

        # Si se encontró el producto 
        nombre = input("Nuevo nombre del producto: ") # Pide al usuario que ingrese el nuevo nombre del producto
        unidad = input("Nueva unidad del producto: ") # Pide al usuario que ingrese la nueva unidad del producto

        
        with open('productos.csv', 'r') as archivo: # Abre el archivo 'productos.csv' en modo lectura
            lector = reader(archivo) # Crea un objeto que puede leer las filas del archivo "productos.csv"
            filas = list(lector)  # Convierte las filas del archivo CSV en una lista de listas

        
        with open('productos.csv', 'w', newline='') as archivo: # Abre el archivo 'productos.csv' en modo escritura
            escritor = writer(archivo)  # Crea un objeto que puede leer las filas del archivo "productos.csv"
            for fila in filas: # Itera sobre todas las filas de la lista de listas
                if fila[0] == sku:  # Si el SKU de la fila actual coincide con el SKU dado por el usuario
                    fila[1] = nombre  # Actualiza el nombre del producto
                    fila[2] = unidad  # Actualiza la unidad del producto
                escritor.writerow(fila)  # Escribe la fila actual en el archivo CSV
        print(f"El producto con SKU '{sku}' ha sido actualizado exitosamente.")  # Imprime un mensaje en la consola
        return True  # Retorna True, indicando que se pudo actualizar el producto

    except Exception as e:  # Si ocurre alguna excepción durante la ejecución del código en el bloque try
        print(f"Error actualizarProducto(): {e.args}")  # Imprime un mensaje de error en la consola
        return False  # Retorna False, indicando que no se pudo actualizar el producto

  def buscarProducto(self) -> bool:  # Método para buscar un producto
    print("Buscar Producto")  # Imprime el mensaje "Buscar Producto" para verificar que se esté invocando al método de forma correcta.
    try:  # Prueba el código y si ocurre una excepción la atrapa
      with open("productos.csv", "r") as file:  # Abre el archivo csv en modo "read" para leer el contenido del archivo
        reader = csv.reader(file, delimiter=",")  # Crea un objeto reader para leer los registros separados por el delimitador ","
        nombre = input("Ingrese el SKU del producto a buscar: ")  # Pide al usuario ingresar el nombre del producto a buscar
        for row in reader:  # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
          if row[0] == nombre:  # Si el primer elemento de la fila coincide con el nombre ingresado por el usuario
            print(f"Registro encontrado: {row}")  # Muestra en consola los datos del registro encontrado
            return True  # Regresa True si el registro se encontró correctamente
        print("No se encontró ningún registro con el nombre ingresado")  # Muestra un mensaje en consola indicando que no se encontró ningún registro con el nombre ingresado por el usuario
        return False  # Regresa False si no se encontró ningún registro con el nombre ingresado por el usuario
    except Exception as e:  # Atrapa cualquier excepción
      print(f"Error buscarProducto(): {e.args}")  # Muestra en consola el error que ocurrió
      return False  # Regresa False si ocurrió un error en el método

  def borrarProducto(self) -> bool:
    print("Borrar Producto")
    sku = input("Ingrese el SKU del producto que desea borrar: ")  # Pide al usuario el SKU del producto que desea borrar
    try:  # Prueba el código y si ocurre una excepción la atrapa
      with open("productos.csv","r") as file:  # Abre el archivo para tener acceso a los registros
        reader = csv.reader(file, delimiter=",")  # Crea un objeto reader para leer los registros separándolos por el delimitador ,
        rows = list(reader)  # Convierte los registros a una lista de filas
      with open("productos.csv", "w", newline="") as file:  # Abre el archivo en modo "w" para escribir los registros
        writer = csv.writer(file, delimiter=",")  # Crea un objeto writer para escribir los registros separándolos por el delimitador ,
        for row in rows:  # Recorre todas las filas encontradas
          if row[0] == sku:  # Si el SKU de la fila es igual al SKU del producto a borrar, no escribe la fila en el archivo
            print(f"Producto '{row[1]}' borrado exitosamente.")  # Imprime un mensaje indicando que el producto fue borrado exitosamente
          else:  # Si el SKU de la fila no es igual al SKU del producto a borrar, escribe la fila en el archivo
            writer.writerow(row) # Escribe una nueva fila en el archivo "productos.csv" con los valores que se han especificado en la lista "row".
      return True  # Regresa True si el método se ejecutó correctamente
    except Exception as e:  # Atrapa cualquier excepción
      print(f"Error borrarProducto(): {e.args}")  # Muestra en consola el error que ocurrió
      return False  # Regresa False si ocurrió un error en el método
