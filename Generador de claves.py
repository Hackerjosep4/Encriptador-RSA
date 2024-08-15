from sympy import primerange
from random import choice
from math import gcd

def generar_numero_primo_aleatorio(rango_min, rango_max):
    primos = list(primerange(rango_min, rango_max))
    return choice(primos)

def encontrar_coprimo_mas_alto(n):
    candidatos = []
    for candidato in range(n - 1, 0, -1):
        if gcd(n, candidato) == 1:
            candidatos.append(candidato)
    if len(candidatos) <= 0:
        return None
    elif len(candidatos) <= 2:
        return candidatos[0]
    else:
        candidatos.pop()
        return choice(candidatos)

def euler(a, b):
    return (a-1)*(b-1)

respuesta = ""
while not respuesta in ["P", "B", "M", "A"]:
    print("Nivel de encriptado:")
    print("\tP - Prueva")
    print("\tB - Bajo")
    print("\tM - Medio")
    print("\tA - Alto")
    respuesta = input("Respuesta: ").strip().upper()
    print()

rangoMin = 0
rangoMax = 0

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

p = generar_numero_primo_aleatorio(rangoMin, rangoMax)
q = generar_numero_primo_aleatorio(rangoMin, rangoMax)
n = p*q
e = encontrar_coprimo_mas_alto(euler(p, q))
d = pow(e, -1, euler(p, q))

print("100% Compleated")
print()

codigoClave = input("Introduce un codigo para la clave: ").strip()

with open(f"Clave_publica({codigoClave}).txt", 'w') as archivo:
    archivo.write(f"{e}, {n}\ne, n")

with open(f"Clave_privada({codigoClave}).txt", 'w') as archivo:
    archivo.write(f"{p}, {q}, {n}, {e}, {d}\np, q, n, e, d")