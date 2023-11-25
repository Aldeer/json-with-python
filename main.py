import json
from datetime import datetime

# ruta del arhcivo json
ruta_archivo = "datos.json"


def crearRegistro():
    # variable bandera
    registrosExist = False

    # lista donde se almacenaran los registros existentes en el archivo json
    registros = list()

    # peticion de datos al usuario mediante inputs
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    creadoEn = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # creando diccionario con los datos almacenados en las variables
    registro = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "creado": creadoEn
    }

    # abrir el archivo json para guardar el diccionario
    try:
        with open(ruta_archivo) as archivo:
            registros = json.load(archivo)
            registrosExist = True
    except Exception as e:
        print(e)

    # condicion que se ejecuta si el archivo json se encuentra vacio o no
    if not registrosExist:
        try:
            with open(ruta_archivo, "w") as archivo:
                registros.append(registro)
                json.dump(registros, archivo, indent=4)
        except Exception as e:
            print("Ha ocurrido un error inesperado: {e}")
    else:
        try:
            with open(ruta_archivo, "w") as archivo:
                registros.append(registro)
                json.dump(registros, archivo, indent=4)
        except Exception as e:
            print("Ha ocurrido un error inesperado: {e}")


crearRegistro()
