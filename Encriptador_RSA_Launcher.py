# INDICE
#
# 1: Imports                        Linea: 
# 2: Funciones                      Linea: Importadas desde Funciones.py
# 3: Iniciar ventana principal      Linea: 
# 4: Variables                      Linea: 
# 5: Codigo                         Linea: 
# 6: Maninloop ventana principal    Linea: 
# 7: Finalizar programa             Linea:
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 










# 1: Imports

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
# Importar funciones
from Funciones import *
# Para manejar json
import json










# 3: Iniciar ventana principal

ventanaPrincipal = tk.Tk()
ventanaPrincipal.geometry("250x100")
ventanaPrincipal.title("Iniciando...")
text1v0 = tk.Label(ventanaPrincipal, text= "Iniciando...")
text1v0.pack(expand= True)










# 4: Variables

# Iniciar variables










# 5: Codigo

loadVentana1(ventanaPrincipal)










# 6: Mainloop ventana principal

ventanaPrincipal.mainloop()










# 7: Finalizar programa

exit()