# Imports
# Libreria para la parte grafica
import tkinter as tk
# Ventana de seleccion
from tkinter import filedialog
# Funcion para comprovar si un archivo existe
from os.path import exists as archivoExiste
# Libreria os
import os
# ...
from sympy import primerange
# ...
from sympy import mod_inverse
# ...
from random import choice
# ...
from math import gcd
# Para manejar json
import json





# Loads Ventanas





def loadVentana1(ventanaPrincipal):
    vaciarVentanaPrincipal(ventanaPrincipal)

    ventanaPrincipal.title("Menu")
    ventanaPrincipal.geometry("200x160")

    tk.Label(ventanaPrincipal, text= "Que quieres hacer?").pack()
    tk.Button(ventanaPrincipal, text= "Encriptar", command= lambda: loadVentanaE1(ventanaPrincipal)).pack()
    tk.Button(ventanaPrincipal, text= "Desencriptar", command= lambda: loadVentanaD1(ventanaPrincipal)).pack()
    tk.Button(ventanaPrincipal, text= "Generar claves", command= lambda: loadVentanaG1(ventanaPrincipal)).pack()
    tk.Button(ventanaPrincipal, text= "Configuracion", command= lambda: loadVentanaC1(ventanaPrincipal)).pack()
    tk.Button(ventanaPrincipal, text= "Salir", command= lambda: cerrar(ventanaPrincipal)).pack()





# Encriptar





def loadVentanaE1(ventanaPrincipal):
    vaciarVentanaPrincipal(ventanaPrincipal)

    ventanaPrincipal.title("Encriptador")
    ventanaPrincipal.geometry("250x100")

    tk.Label(ventanaPrincipal, text= "Desactivado").pack()
    tk.Button(ventanaPrincipal, text= "Atras", command= lambda : loadVentana1(ventanaPrincipal)).pack()





# Desencriptar





def loadVentanaD1(ventanaPrincipal):
    vaciarVentanaPrincipal(ventanaPrincipal)

    ventanaPrincipal.title("Desencriptador")
    ventanaPrincipal.geometry("250x100")

    tk.Label(ventanaPrincipal, text= "Desactivado").pack()
    tk.Button(ventanaPrincipal, text= "Atras", command= lambda : loadVentana1(ventanaPrincipal)).pack()





# Generar claves





def loadVentanaG1(ventanaPrincipal):
    vaciarVentanaPrincipal(ventanaPrincipal)

    ventanaPrincipal.title("Generador")
    ventanaPrincipal.geometry("200x300")

    tk.Label(ventanaPrincipal, text= "Selecciona una opcion").pack()
    tk.Button(ventanaPrincipal, text= "Prueva", command= lambda: generar_claves(ventanaPrincipal, 16, 50)).pack()
    tk.Button(ventanaPrincipal, text= "Sencillo", command= lambda: generar_claves(ventanaPrincipal, 50, 100)).pack()
    tk.Button(ventanaPrincipal, text= "Basico", command= lambda: generar_claves(ventanaPrincipal, 100, 1000)).pack()
    tk.Button(ventanaPrincipal, text= "Bajo", command= lambda: generar_claves(ventanaPrincipal, 1000, 10000)).pack()
    tk.Button(ventanaPrincipal, text= "Medio", command= lambda: generar_claves(ventanaPrincipal, 10000, 100000)).pack()
    tk.Button(ventanaPrincipal, text= "Alto", command= lambda: generar_claves(ventanaPrincipal, 100000, 500000)).pack()
    tk.Button(ventanaPrincipal, text= "Muy alto", command= lambda: generar_claves(ventanaPrincipal, 500000, 1000000)).pack()
    tk.Button(ventanaPrincipal, text= "Extremo", command= lambda: generar_claves(ventanaPrincipal, 1000000, 10000000)).pack()
    tk.Button(ventanaPrincipal, text= "Ultra extremo", command= lambda: generar_claves(ventanaPrincipal, 10000000, 100000000)).pack()
    tk.Button(ventanaPrincipal, text= "Atras", command= lambda: loadVentana1(ventanaPrincipal)).pack()






# Configuracion





def loadVentanaC1(ventanaPrincipal):
    vaciarVentanaPrincipal(ventanaPrincipal)

    ventanaPrincipal.title("Configuracion")
    ventanaPrincipal.geometry("200x175")

    tk.Label(ventanaPrincipal, text= "Desactivado temporalmente").pack()
    tk.Label(ventanaPrincipal, text= "Que quieres configurar?").pack()
    tk.Button(ventanaPrincipal, text="Clave publica").pack()
    tk.Button(ventanaPrincipal, text="Clave privada").pack()
    tk.Button(ventanaPrincipal, text="Personas").pack()
    tk.Button(ventanaPrincipal, text="Grupos").pack()
    tk.Button(ventanaPrincipal, text="Atras", command= lambda : loadVentana1(ventanaPrincipal)).pack()





# Funciones de botones





def funButton1():
    pass





# Otras funciones





# Para cerrar el codigo en caso de error
def cerrarPorError(textError = "Unknow"):
    # Crear una ventana secundaria para el mensage
    ventanaError = tk.Toplevel()
    # Añadir los textos
    text1vE = tk.Label(ventanaError, text= "Error:")
    text2vE = tk.Label(ventanaError, text= textError)
    text1vE.pack()
    text2vE.pack()
    # Hacer que finalize el codigo despues de 5 segundos
    ventanaError.after(5000, exit)
    # Llamar al mainloop
    ventanaError.mainloop()
    # Para que se cierre el codigo en caso que salga del mainloop
    exit()

# Cerrar el programa
def cerrar(ventanaPrincipal):
    ventanaPrincipal.destroy()
    # Cerrar codigo
    exit()

# Para vaciar la ventana principal y añadir elementos desde cero
def vaciarVentanaPrincipal(ventanaPrincipal):
    for elemento in ventanaPrincipal.winfo_children():
        elemento.destroy()
    ventanaPrincipal.geometry("100x100")
    ventanaPrincipal.title("")

def encriptar(e, n, mensage):
    textoEncriptado=[]

    for caracterDesencriptado in mensage:
        # Aplica la fórmula de encriptación RSA: (carácter^e) % n
        caracterEncriptado = pow(caracterDesencriptado, e, n)
        # Añade el carácter encriptado a la lista
        textoEncriptado.append(caracterEncriptado)

    mensageEncriptado = ', '.join(str(numero) for numero in textoEncriptado)
    
    with open(filedialog.asksaveasfilename( defaultextension=".txt", filetypes=[("Text files", "*.txt")], title="Guardar archivo como" ), 'w') as archivo:
            archivo.write(mensageEncriptado)

def desencriptar(d, n, mensage):
    textoEncriptado = mensage.split(", ")
    textoDesencriptado = []

    for caracterEncriptado in textoEncriptado:
        # Aplica la fórmula de encriptación RSA: (carácter^d) % n
        caracterDesencriptado = pow(caracterEncriptado, d, n)
        # Añade el carácter encriptado a la lista
        textoDesencriptado.append(caracterDesencriptado)
    
    mensageDesencriptado = "".join(textoDesencriptado)
    
    with open(filedialog.asksaveasfilename( defaultextension=".txt", filetypes=[("Text files", "*.txt")], title="Guardar archivo como" ), 'w') as archivo:
            archivo.write(mensageDesencriptado)

# Función para generar un número primo aleatorio dentro de un rango dado
def generar_numero_primo_aleatorio(rango_min, rango_max):
    # Obtiene una lista de números primos en el rango especificado
    primos = list(primerange(rango_min, rango_max))
    # Elige aleatoriamente un número primo de la lista
    return choice(primos)

# Función para encontrar el coprimo más alto de un número n
def encontrar_coprimo_aleatorio(n):
    candidatos = []
    if n%2 == 0:
        # Itera en orden descendente desde n-1 hasta 1
        for candidato in range(n - 1, 0, -2):
            # Verifica si el candidato es coprimo con n usando el máximo común divisor
            if gcd(n, candidato) == 1:
                # Si es coprimo, lo añade a la lista de candidatos
                candidatos.append(candidato)
                if len(candidatos) > 10000000:
                    break
    else:
        # Itera en orden descendente desde n-1 hasta 1
        for candidato in range(n - 1, 0, -1):
            # Verifica si el candidato es coprimo con n usando el máximo común divisor
            if gcd(n, candidato) == 1:
                # Si es coprimo, lo añade a la lista de candidatos
                candidatos.append(candidato)
                if len(candidatos) > 10000000:
                    break
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

# Funcion para crear las claves
def generar_claves(ventanaPrincipal, rangoMin, rangoMax):
    ventana_loading = tk.Toplevel()
    ventana_loading.title("Loading")
    ventana_loading.geometry("200x100")
    tk.Label(ventana_loading, text= "Loading...").pack()

    # Genera dos números primos aleatorios en el rango especificado
    p = generar_numero_primo_aleatorio(rangoMin, rangoMax)
    q = generar_numero_primo_aleatorio(rangoMin, rangoMax)
    # Calcula n como el producto de p y q
    n = p*q
    # Calcula el valor de e como el coprimo más alto de la función totiente de Euler de p y q
    e = encontrar_coprimo_aleatorio(euler(p, q))
    # Calcula el valor de d como el inverso multiplicativo de e módulo la función totiente de Euler de p y q
    #d = pow(e, -1, euler(p, q))
    d = mod_inverse(e, euler(p, q))

    # Solicita al usuario un código para identificar la clave
    codigoClave = ""
    while codigoClave == "":
        codigoClave = str(tk.simpledialog.askstring("Input", "Introduce el codigo para las claves")).strip()
    
    rutaGuardado = tk.filedialog.askdirectory()

    # Guarda la clave pública en un archivo
    with open(f"{rutaGuardado}\\Clave_publica({codigoClave}).txt", 'w') as archivo:
        archivo.write(f"{e}, {n}\ne, n")

    # Guarda la clave privada en un archivo
    with open(f"{rutaGuardado}\\Clave_privada({codigoClave}).txt", 'w') as archivo:
        archivo.write(f"{p}, {q}, {n}, {e}, {d}\np, q, n, e, d")

    ventana_loading.destroy()

    loadVentana1(ventanaPrincipal)

def leerConfigPri():
    with open(f"{os.path.dirname(__file__)}\\configs\\pri.json", 'r') as archivo:
        config = json.load(archivo)
    
    return config

def leerConfigPub():
    with open(f"{os.path.dirname(__file__)}\\configs\\pub.json", 'r') as archivo:
        config = json.load(archivo)
    
    return config

def leerConfigPer():
    with open(f"{os.path.dirname(__file__)}\\configs\\per.json", 'r') as archivo:
        config = json.load(archivo)
    
    return config

def leerConfigGru():
    with open(f"{os.path.dirname(__file__)}\\configs\\gru.json", 'r') as archivo:
        config = json.load(archivo)
    
    return config

def escribirConfigPri(config):
    with open(f"{os.path.dirname(__file__)}\\configs\\pri.json", 'w') as archivo:
        json.dump(config)

def escribirConfigPub(config):
    with open(f"{os.path.dirname(__file__)}\\configs\\pub.json", 'w') as archivo:
        json.dump(config)

def escribirConfigPer(config):
    with open(f"{os.path.dirname(__file__)}\\configs\\per.json", 'w') as archivo:
        json.dump(config)

def escribirConfigGru(config):
    with open(f"{os.path.dirname(__file__)}\\configs\\gru.json", 'w') as archivo:
        json.dump(config)