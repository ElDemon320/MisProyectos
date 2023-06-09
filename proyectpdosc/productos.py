import csv  # Librería para abrir, leer y escribir archivos CSV
from csv import writer  # Importa el módulo "writer" de la librería "csv"# Importa el módulo "writer" de la librería "csv"


class Productos:  # Clase Productos

  def __init__(self):  # Constructor de la clase Productos
    pass  # Inicializa el objeto de la clase Productos

  def listarProductos(
      self) -> bool:  # Metodo para listar los productos registrados
    print("Listado de Productos")  # Imprime en pantalla el mensaje
    try:  # Prueba el código y si ocurre una excepción la atrapa
      with open(
          "productos.csv",
          "r") as file:  # Abre el archivo para tener acceso a los registros
        reader = csv.DictReader(
          file, delimiter=","
        )  # Crea un objeto reader para leer los registros separándolos por el delimitador ,
        for row in reader:  # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
          print(f"Registro: {row}"
                )  # Imprime los datos del registro como un diccionario
      return True  # Regresa True si el método se ejecutó correctamente
    except Exception as e:  # Atrapa cualquier excepción
      print(f"Error listarProductos() :{e.args}"
            )  # Muestra en consola el error que ocurrió
      return False  # Regresa False si ocurrió un error en el método

  def insertarProducto(self) -> bool: # Metodo para insertar un producto
        print("Función insertarProducto()")  # Imprime el mensaje "Método insertarProducto" para verificar que se esté invocando al método de forma correcta.
        

        sku = input("SKU: ")  # Pide al usuario que introduzca el SKU del producto
        nombre = input("Nombre: ")  # Pide al usuario que introduzca el nombre del producto
        unidad = input("Unidad: ")  # Pide al usuario que introduzca el tipo de unidad del producto

        try: # Prueba el código y si ocurre una excepción la atrapa
            fila_productos = [sku, nombre, unidad]  # Crea una lista con los valores de las variables sku, nombre y unidad.

            print(f"INSERTAR: SKU: {sku}, Nombre: {nombre}, Unidad: {unidad}")

            with open('productos.csv', 'a') as objetoArchivo:  # Abre el archivo "productos.csv" en "append mode" para poder agregar una fila al documento, 
            #                                                    y crea un objeto de este documento para poder trabajarlo. Se guarda como "objetoArchivo".

                objeto_w = writer(objetoArchivo)  # Se consigue un objeto con la función writer() a partir de "objetoArchivo". Se guarda como "objeto_w"
                objeto_w.writerow(fila_productos)  # Se utiliza la lista "fila_productos" como argumento para añadir la nueva fila, haciendo uso de la función writerow()

                objetoArchivo.close()  # Se cierra el objeto del documento "objetoArchivo" con la función close().
            return True # Regresa True si el método se ejecutó correctamente
        except Exception as e: # Atrapa cualquier excepción
            print(f"Error borrarProducto(): {e.args}") # Muestra en consola el error que ocurrió
            return False # Regresa False si ocurrio un error en el metodo

  def actualizarProducto(self, sku: str, nombre: str, unidad: str) -> bool:
    print("Método actualizarProducto()")
    try:
      with open("productos.csv", "r") as file:
        reader = csv.reader(file)
        productos = list(reader)
      for producto in productos:
        if producto[0] == sku:
          producto[1] = nombre
          producto[2] = unidad
      with open("productos.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(productos)
      print(f"Producto con SKU '{sku}' actualizado exitosamente.")
      return True
    except Exception as e:
      print(f"Error actualizarProducto(): {e.args}")
      return False

  def buscarProducto(self) -> bool:  # Método para buscar un producto
    print(
      "Buscar Producto"
    )  # Imprime el mensaje "Buscar Producto" para verificar que se esté invocando al método de forma correcta.
    try:  # Prueba el código y si ocurre una excepción la atrapa
      with open(
          "productos.csv", "r"
      ) as file:  # Abre el archivo csv en modo "read" para leer el contenido del archivo
        reader = csv.reader(
          file, delimiter=","
        )  # Crea un objeto reader para leer los registros separados por el delimitador ","
        nombre = input(
          "Ingrese el nombre del producto a buscar: "
        )  # Pide al usuario ingresar el nombre del producto a buscar
        for row in reader:  # Recorre todos los registros encontrados y almacena temporalmente cada uno en row
          if row[
              0] == nombre:  # Si el primer elemento de la fila coincide con el nombre ingresado por el usuario
            print(f"Registro encontrado: {row}"
                  )  # Muestra en consola los datos del registro encontrado
            return True  # Regresa True si el registro se encontró correctamente
        print(
          "No se encontró ningún registro con el nombre ingresado"
        )  # Muestra un mensaje en consola indicando que no se encontró ningún registro con el nombre ingresado por el usuario
        return False  # Regresa False si no se encontró ningún registro con el nombre ingresado por el usuario
    except Exception as e:  # Atrapa cualquier excepción
      print(f"Error buscarProducto(): {e.args}"
            )  # Muestra en consola el error que ocurrió
      return False  # Regresa False si ocurrió un error en el método

  def borrarProducto(self) -> bool:
    print("Borrar Producto")
    sku = input("Ingrese el SKU del producto que desea borrar: "
                )  # Pide al usuario el SKU del producto que desea borrar
    try:  # Prueba el código y si ocurre una excepción la atrapa
      with open(
          "productos.csv",
          "r") as file:  # Abre el archivo para tener acceso a los registros
        reader = csv.reader(
          file, delimiter=","
        )  # Crea un objeto reader para leer los registros separándolos por el delimitador ,
        rows = list(reader)  # Convierte los registros a una lista de filas
      with open(
          "productos.csv", "w", newline=""
      ) as file:  # Abre el archivo en modo "w" para escribir los registros
        writer = csv.writer(
          file, delimiter=","
        )  # Crea un objeto writer para escribir los registros separándolos por el delimitador ,
        for row in rows:  # Recorre todas las filas encontradas
          if row[
              0] == sku:  # Si el SKU de la fila es igual al SKU del producto a borrar, no escribe la fila en el archivo
            print(
              f"Producto '{row[1]}' borrado exitosamente."
            )  # Imprime un mensaje indicando que el producto fue borrado exitosamente
          else:  # Si el SKU de la fila no es igual al SKU del producto a borrar, escribe la fila en el archivo
            writer.writerow(row)
      return True  # Regresa True si el método se ejecutó correctamente
    except Exception as e:  # Atrapa cualquier excepción
      print(f"Error borrarProducto(): {e.args}"
            )  # Muestra en consola el error que ocurrió
      return False  # Regresa False si ocurrió un error en el método
