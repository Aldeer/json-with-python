import json
from datetime import datetime

# ruta del arhcivo json
ruta_archivo = "datos.json"


def mostrarDatos():

    # Abriendo el archivo de datos json
    try:
        with open(ruta_archivo) as archivo:
            # trasnformando de formato json a tipos de dato en python
            contenido = json.load(archivo)
            # recorriendo el contenido del archivo
            for persona in contenido:
                # imprimiendo por pantalla los datos de las personas guardadas
                # en el archivo json
                print(persona)
    except Exception as e:
        print(f"Se produjo el siguiente error: {e}")


def nuevoRegistro():
    # ingreso del nombre por consola
    nombre = input("Ingrese su nombre: ")
    # ingreso del apellido por consola
    apellido = input("Ingrese su apellido: ")
    # fecha en la que se creo el registro
    creandoEn = datetime.now()


mostrarDatos()
