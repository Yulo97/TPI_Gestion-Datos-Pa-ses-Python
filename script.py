import csv

# Funcion principal
def main():
    print("-----OPCIONES-----")
    print("1 - Agregar un pais")
    print("2 - Actualizar poblacion y superficie")
    print("3 - Buscar un pais por nombre")
    print("4 - Filtrar paises por continente, rango de poblacion y rango de superficie")
    print("5 - Mostrar paises por nombre, poblacion y superfie")
    print("6 - Mostrar estadisticas")
    print("7 - Salir")

    paises = read_file()
    
    opcion = ""

    while(opcion != "7"):
        opcion = input("Ingresa una opcion: ")

        if(opcion == "1"):
            add_pais(paises)
        elif(opcion == "2"):
            update_pais(paises)
        elif(opcion == "3"):
            nombre_pais = input("Ingresa el nombre: ")
            find_pais(paises, nombre_pais)
        elif(opcion == "4"):
            filter_paises(paises)
        elif(opcion == "5"):
            mostrar_paises(paises)
        else:
            break


    print("Termino el programa")

# Funcion para lectura de archivo
def read_file ():
    # Variable vacia donde se guardaran los paises
    paises = []

    # Lectura de csv con la libreria csv
    with open("paises.csv", encoding="utf8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            paises.append({
                "nombre": fila["nombre"],
                "continente": fila["continente"],
                "poblacion": int(fila["poblacion"]),
                "superficie": int(fila["superficie"])
            })

    return paises

# Funcion para agregar un Pais
def add_pais (paises):
    try:
        nombre = input("Nombre: ").strip()
        poblacion = int(input("Poblacion: ").strip())
        superficie = int(input("Superficie: ").strip())
        continente = input("Continente: ").strip()

        if(not nombre or not poblacion or not superficie or not continente):
            print("Debes ingresar todos los datos.")
            return

        paises.append({
            "nombre": nombre,
            "continente": continente,
            "poblacion": poblacion,
            "superficie": superficie
        })

        # Reescribir el archivo CSV con el nuevo país
        write_file_paises(paises)

        print("\nAgregaste los datos correctamente")
    except ValueError:
        print("Error: Debes ingresar datos validos")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

# Funcion para buscar pais por nombre
def find_pais(paises, nombre_pais):
    for pais in paises:
        if(nombre_pais in pais["nombre"]):
            print(pais)

# Funcion para actualizar superfice
def update_pais(paises):
    nombre_pais = input("Ingresa el nombre del pais a actualizar: ").lower()
    pais_encontrado = ""

    for pais in paises:
        if(nombre_pais.lower() == pais["nombre"].lower()):
            pais_encontrado = pais
    
    if(pais_encontrado == ""):
        print("No se encontro el pais para actualizar")
        return
    else:
        poblacion = int(input("Poblacion: "))
        superficie = int(input("Superficie: "))

        pais_encontrado["poblacion"] = poblacion
        pais_encontrado["superficie"] = superficie

        write_file_paises(paises)

def write_file_paises(paises):
    # Reescribir el archivo CSV con el nuevo país
    with open("paises.csv", "w", encoding="utf8", newline="") as f:
        fieldnames = ["nombre", "continente", "poblacion", "superficie"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for pais in paises:
            writer.writerow(pais)

def filter_paises(paises):
    print("-----OPCIONES-----")
    print("1 - Filtrar por Continente")
    print("2 - Filtrar por Superfice")
    print("3 - Filtrar por Poblacion")

    opcion_filtro = input("Ingresa una opcion: ")

    if(opcion_filtro == "1"):
        continente = input("Ingresa un continente: ").lower()

        for pais in paises:
            if(continente.lower() == pais["continente"].lower()):
                print(pais) 
    elif(opcion_filtro == "2"):
        superficie_minima = int(input("Ingrese una superficie minima: "))
        superficie_maxima = int(input("Ingrese una superficie maxima: "))

        for pais in paises:
            if(superficie_minima <= pais["superficie"] and superficie_maxima >= pais["superficie"]):
                print(pais) 

    elif(opcion_filtro == "3"):
        poblacion_minima = int(input("Ingrese una poblacion minima: "))
        poblacion_maxima = int(input("Ingrese una poblacion maxima: "))

        for pais in paises:
            if(poblacion_minima <= pais["poblacion"] and poblacion_maxima >= pais["poblacion"]):
                print(pais) 

def mostrar_paises(paises):
    print("-----OPCIONES-----")
    print("1 - Ordenar por nombre")
    print("2 - Ordenar por poblacion")
    print("3 - Ordenar por superficie")

    opcion = input("Ingresa una opcion: ")

    if(opcion == "1"):
        paises_ordenados = sorted(paises, key=lambda pais: pais["nombre"].lower())
    elif(opcion == "2"):
        paises_ordenados = sorted(paises, key=lambda pais: pais["poblacion"])
    elif(opcion == "3"):
        orden = input("¿Ascendente o descendente? (a/d): ").strip().lower()
        reverse = False
        if orden == "d":
            reverse = True
        elif orden != "a":
            print("Opcion de orden invalida, se usara ascendente por defecto.")

        paises_ordenados = sorted(paises, key=lambda pais: pais["superficie"], reverse=reverse)
    else:
        print("Opcion invalida")
        return

    for pais in paises_ordenados:
        print(pais)


main()
