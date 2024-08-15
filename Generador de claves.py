from sympy import primerange
from random import choice
from math import gcd

# Función para generar un número primo aleatorio dentro de un rango dado
def generar_numero_primo_aleatorio(rango_min, rango_max):
    # Obtiene una lista de números primos en el rango especificado
    primos = list(primerange(rango_min, rango_max))
    # Elige aleatoriamente un número primo de la lista
    return choice(primos)

# Función para encontrar el coprimo más alto de un número n
def encontrar_coprimo_mas_alto(n):
    candidatos = []
    # Itera en orden descendente desde n-1 hasta 1
    for candidato in range(n - 1, 0, -1):
        # Verifica si el candidato es coprimo con n usando el máximo común divisor
        if gcd(n, candidato) == 1:
            # Si es coprimo, lo añade a la lista de candidatos
            candidatos.append(candidato)
    # Si no se encontraron candidatos, retorna None
    if len(candidatos) <= 0:
        return None
    # Si hay uno o dos candidatos, retorna el primero de la lista
    elif len(candidatos) <= 2:
        return candidatos[0]
    else:
        # Elimina el último candidato de la lista
        candidatos.pop()
        # Retorna un candidato aleatorio de la lista restante
        return choice(candidatos)

# Función para calcular la función totiente de Euler para dos números primos
def euler(a, b):
    return (a-1)*(b-1)

respuesta = ""
# Bucle que se ejecuta hasta que el usuario introduzca una opción válida
while not respuesta in ["P", "B", "M", "A"]:
    # Imprime las opciones para el nivel de encriptado
    print("Nivel de encriptado:")
    print("\tP - Prueva")
    print("\tB - Bajo")
    print("\tM - Medio")
    print("\tA - Alto")
    # Captura la respuesta del usuario, eliminando espacios y convirtiéndola a mayúsculas
    respuesta = input("Respuesta: ").strip().upper()
    print()

# Inicializa los rangos mínimo y máximo
rangoMin = 0
rangoMax = 0

# Define el rango de números primos basado en la opción del usuario
if respuesta == "P":
    rangoMin = 10
    rangoMax = 50
elif respuesta == "B":
    rangoMin = 100
    rangoMax = 1000
elif respuesta == "M":
    rangoMin = 1000
    rangoMax = 10000
else:
    rangoMin = 10000
    rangoMax = 100000

print()
print("Loading...")

# Genera dos números primos aleatorios en el rango especificado
p = generar_numero_primo_aleatorio(rangoMin, rangoMax)
q = generar_numero_primo_aleatorio(rangoMin, rangoMax)
# Calcula n como el producto de p y q
n = p*q
# Calcula el valor de e como el coprimo más alto de la función totiente de Euler de p y q
e = encontrar_coprimo_mas_alto(euler(p, q))
# Calcula el valor de d como el inverso multiplicativo de e módulo la función totiente de Euler de p y q
d = pow(e, -1, euler(p, q))

print("100% Compleated")
print()

# Solicita al usuario un código para identificar la clave
codigoClave = input("Introduce un codigo para la clave: ").strip()

# Guarda la clave pública en un archivo
with open(f"Clave_publica({codigoClave}).txt", 'w') as archivo:
    archivo.write(f"{e}, {n}\ne, n")

# Guarda la clave privada en un archivo
with open(f"Clave_privada({codigoClave}).txt", 'w') as archivo:
    archivo.write(f"{p}, {q}, {n}, {e}, {d}\np, q, n, e, d")
