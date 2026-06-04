# TPI_Gestion-Datos-Paises-Python

Descripción
-----------

Proyecto para gestionar y analizar un conjunto de datos de países almacenado en formato CSV. Contiene un script (`script.py`) que carga el archivo `paises.csv` y permite procesar/visualizar la información de cada país.

Uso
----

- Requisitos: Python 3.8+.
- Colocar el archivo `paises.csv` en la raíz del proyecto (ya incluido en este repositorio).
- Ejecutar el script desde la raíz del proyecto:

```
python script.py
```

Si prefiere ejecutar con una ruta distinta, abra `script.py` y modifique la variable o argumento que indica la ruta del archivo de entrada.

Formato de entrada (ejemplo)
---------------------------

El CSV esperado tiene una cabecera y filas con los campos separados por comas. Ejemplo (primeras líneas de `paises.csv`):

```
nombre,continente,poblacion,superficie
Argentina,America,123,123
Japon,Asia,125800000,377975
Brasil,America,213993437,8515767
Alemania,Europa,83149300,357022
```

Ejemplos de salida
------------------

El formato de salida dependerá de la lógica implementada en `script.py`. A modo de ejemplo, el script podría mostrar:

```
Total registros: 6
Listado (nombre - continente - población - superficie):
- Argentina - America - 123 - 123
- Japon - Asia - 125800000 - 377975
- Brasil - America - 213993437 - 8515767
```

Participación de los integrantes
-------------------------------

- Nombre: Manchini María Virginia — Rol: Desarrollador
- Nombre: De Vito Giuliano — Rol: Desarrollador

Repositorio
-----

- https://github.com/Yulo97/TPI_Gestion-Datos-Pa-ses-Python

Notas
-----

- Para dudas o mejoras, abra un issue o contacte a los integrantes listados arriba.
