# ==============================
# Sistema de Evaluación Académica
# Versión inicial con listas y matrices
# ==============================

# Función para cargar alumnos
def cargar_alumnos():
    alumnos = []
    n = int(input("Ingrese la cantidad de alumnos: "))
    for i in range(n):
        nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
        alumnos.append(nombre)
    return alumnos

# Función para cargar materias
def cargar_materias():
    materias = []
    m = int(input("Ingrese la cantidad de materias: "))
    for j in range(m):
        materia = input(f"Ingrese el nombre de la materia {j+1}: ")
        materias.append(materia)
    return materias

# Crear matriz vacía de calificaciones
def crear_matriz(filas, columnas):
    return [[0]*columnas for _ in range(filas)]

# Cargar calificaciones en la matriz
def cargar_calificaciones(matriz, alumnos, materias):
    for i in range(len(alumnos)):
        for j in range(len(materias)):
            nota = int(input(f"Ingrese la nota de {alumnos[i]} en {materias[j]}: "))
            matriz[i][j] = nota

# Imprimir matriz de calificaciones
def imprimir_calificaciones(matriz, alumnos, materias):
    print("\n--- Calificaciones ---")
    print("Alumno".ljust(12), end="")
    for mat in materias:
        print(mat.ljust(10), end="")
    print()
    for i in range(len(alumnos)):
        print(alumnos[i].ljust(12), end="")
        for j in range(len(materias)):
            print(str(matriz[i][j]).ljust(10), end="")
        print()

# Calcular promedios de cada alumno
def calcular_promedios(matriz, alumnos):
    print("\n--- Promedios de Alumnos ---")
    for i in range(len(alumnos)):
        promedio = sum(matriz[i]) / len(matriz[i])
        print(f"{alumnos[i]}: {promedio:.2f}")

# ==============================
# Programa principal
# ==============================
alumnos = cargar_alumnos()
materias = cargar_materias()
notas = crear_matriz(len(alumnos), len(materias))
cargar_calificaciones(notas, alumnos, materias)
imprimir_calificaciones(notas, alumnos, materias)
calcular_promedios(notas, alumnos)
