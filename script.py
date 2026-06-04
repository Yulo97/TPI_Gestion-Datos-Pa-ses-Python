import csv

# Funcion principal
def main():
    print("-----OPCIONES-----")
    print("1 - Agregar un pais")
    print("2 - Actualizar poblacion y superficie")
    print("3 - Buscar un pais por nombre")
    print("4 - Filtrar paises por continente, rango de poblacion y rango de superficie")
    print("5 - Mostrar paises por nombre, poblacion y superficie")
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
        elif(opcion == "6"):
            mostrar_estadisticas(paises)
        elif(opcion == "7"):
            break
        else:
            print("Opcion invalida. Intenta nuevamente.")

    print("Termino el programa")

# Funcion para lectura de archivo
def read_file():
    # Variable vacia donde se guardaran los paises
    paises = []

    try:
        with open("paises.csv", encoding="utf8") as f:
            reader = csv.DictReader(f)
            for fila in reader:
                paises.append({
                    "nombre": fila["nombre"],
                    "continente": fila["continente"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"])
                })
    except FileNotFoundError:
        print("Archivo paises.csv no encontrado. Se iniciara con lista vacia.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

    return paises

# Funcion para agregar un Pais
def add_pais(paises):
    try:
        nombre = input("Nombre: ").strip()
        poblacion_texto = input("Poblacion: ").strip()
        superficie_texto = input("Superficie: ").strip()
        continente = input("Continente: ").strip()

        if not nombre or not poblacion_texto or not superficie_texto or not continente:
            print("Debes ingresar todos los datos.")
            return

        poblacion = int(poblacion_texto)
        superficie = int(superficie_texto)

        paises.append({
            "nombre": nombre,
            "continente": continente,
            "poblacion": poblacion,
            "superficie": superficie
        })

        write_file_paises(paises)
        print("\nAgregaste los datos correctamente")
    except ValueError:
        print("Error: Debes ingresar datos validos para poblacion y superficie.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

# Funcion para buscar pais por nombre
def find_pais(paises, nombre_pais):
    resultados = []
    termino = nombre_pais.strip().lower()

    for pais in paises:
        if termino in pais["nombre"].lower():
            resultados.append(pais)

    if resultados:
        for pais in resultados:
            print(pais)
    else:
        print("No se encontro ningun pais con ese nombre.")

# Funcion para actualizar superficie y poblacion
def update_pais(paises):
    nombre_pais = input("Ingresa el nombre del pais a actualizar: ").strip().lower()
    pais_encontrado = None

    for pais in paises:
        if nombre_pais == pais["nombre"].lower():
            pais_encontrado = pais
            break

    if pais_encontrado is None:
        print("No se encontro el pais para actualizar")
        return

    try:
        poblacion = int(input("Poblacion: ").strip())
        superficie = int(input("Superficie: ").strip())
        pais_encontrado["poblacion"] = poblacion
        pais_encontrado["superficie"] = superficie
        write_file_paises(paises)
        print("Datos actualizados correctamente.")
    except ValueError:
        print("Error: Debes ingresar valores numericos validos.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

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
    print("2 - Filtrar por Superficie")
    print("3 - Filtrar por Poblacion")

    opcion_filtro = input("Ingresa una opcion: ")
    resultados = []

    if opcion_filtro == "1":
        continente = input("Ingresa un continente: ").strip().lower()
        for pais in paises:
            if continente == pais["continente"].lower():
                resultados.append(pais)
    elif opcion_filtro == "2":
        try:
            superficie_minima = int(input("Ingrese una superficie minima: ").strip())
            superficie_maxima = int(input("Ingrese una superficie maxima: ").strip())
            for pais in paises:
                if superficie_minima <= pais["superficie"] <= superficie_maxima:
                    resultados.append(pais)
        except ValueError:
            print("Error: Debes ingresar numeros validos para superficie.")
            return
    elif opcion_filtro == "3":
        try:
            poblacion_minima = int(input("Ingrese una poblacion minima: ").strip())
            poblacion_maxima = int(input("Ingrese una poblacion maxima: ").strip())
            for pais in paises:
                if poblacion_minima <= pais["poblacion"] <= poblacion_maxima:
                    resultados.append(pais)
        except ValueError:
            print("Error: Debes ingresar numeros validos para poblacion.")
            return
    else:
        print("Opcion invalida")
        return

    if resultados:
        for pais in resultados:
            print(pais)
    else:
        print("No se encontraron paises con esos criterios.")

def mostrar_paises(paises):
    print("-----OPCIONES-----")
    print("1 - Ordenar por nombre")
    print("2 - Ordenar por poblacion")
    print("3 - Ordenar por superficie")

    opcion = input("Ingresa una opcion: ")
    orden = input("¿Ascendente o descendente? (a/d): ").strip().lower()
    reverse = orden == "d"

    if orden not in ["a", "d"]:
        print("Opcion de orden invalida, se usara ascendente por defecto.")
        reverse = False

    if opcion == "1":
        paises_ordenados = sorted(paises, key=lambda pais: pais["nombre"].lower(), reverse=reverse)
    elif opcion == "2":
        paises_ordenados = sorted(paises, key=lambda pais: pais["poblacion"], reverse=reverse)
    elif opcion == "3":
        paises_ordenados = sorted(paises, key=lambda pais: pais["superficie"], reverse=reverse)
    else:
        print("Opcion invalida")
        return

    for pais in paises_ordenados:
        print(pais)


def mostrar_estadisticas(paises):
    if not paises:
        print("No hay datos de paises para mostrar estadisticas.")
        return

    mayor_poblacion = max(paises, key=lambda pais: pais["poblacion"])
    menor_poblacion = min(paises, key=lambda pais: pais["poblacion"])
    promedio_poblacion = sum(p["poblacion"] for p in paises) / len(paises)
    promedio_superficie = sum(p["superficie"] for p in paises) / len(paises)

    conteo_continentes = {}
    for pais in paises:
        continente = pais["continente"]
        conteo_continentes[continente] = conteo_continentes.get(continente, 0) + 1

    print(f"Pais con mayor poblacion: {mayor_poblacion['nombre']} ({mayor_poblacion['poblacion']})")
    print(f"Pais con menor poblacion: {menor_poblacion['nombre']} ({menor_poblacion['poblacion']})")
    print(f"Promedio de poblacion: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f}")
    print("Cantidad de paises por continente:")
    for continente, cantidad in conteo_continentes.items():
        print(f"- {continente}: {cantidad}")


main()