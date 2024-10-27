# INDICE
#
# 1: Imports                        Linea: 
# 2: Funciones                      Linea: 
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
# Ventana0  : Inicializar
# Ventana1  : Preguntgar Automatico o Manual
# Ventana1a : Pedir valores Automatico
# Ventana1b : Pedir valores Manual
# Ventana2  : Abrir mensage encriptado
# Ventana3  : Desencriptar
# Ventana4  : Guardar mensage desencriptado
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
#
from tkinter import filedialog
# Funcion para comprovar si un archivo existe
from os.path import exists as archivoExiste










# 2: Funciones

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
def cerrar():
    # Llamar a la ventana principal
    global ventanaPrincipal
    # Cerrar ventana principal
    ventanaPrincipal.destroy()
    # Cerrar codigo
    exit()

# Para vaciar la ventana principal y añadir elementos desde cero
def vaciarVentanaPrincipal():
    # Llamar a las variables globales
    global ventanaPrincipal
    # Destruir cada elemento de la ventana principal
    for elemento in ventanaPrincipal.winfo_children():
        elemento.destroy()
    ventanaPrincipal.geometry("100x100")
    ventanaPrincipal.title("")

def loadVentana1():
    global ventanaPrincipal

    vaciarVentanaPrincipal()

    ventanaPrincipal.title("Desencriptador")
    ventanaPrincipal.geometry("250x100")

    text1v1 = tk.Label(ventanaPrincipal, text= "Como quieres introducir los datos?")
    button1v1 = tk.Button(ventanaPrincipal, text= "Automatico", command= loadVentana1a)
    button2v1 = tk.Button(ventanaPrincipal, text= "Manual", command= loadVentana1b)

    text1v1.pack()
    button1v1.pack()
    button2v1.pack()

def loadVentana1a():
    global ventanaPrincipal

    vaciarVentanaPrincipal()

    ventanaPrincipal.title("Automatico")
    ventanaPrincipal.geometry("750x100")

    text1v1a = tk.Label(ventanaPrincipal, text= "Seleccione el archivo con la clave")
    text2v1a = tk.Label(ventanaPrincipal, text= "Sin seleccionar")
    button1v1a = tk.Button(ventanaPrincipal, text= "Seleccionar archivo", command= lambda: text2v1a.configure(text= funbutton1v1a()))
    button2v1a = tk.Button(ventanaPrincipal, text= "Continuar", command= funbutton2v1a)

    text1v1a.pack()
    text2v1a.pack()
    button1v1a.pack()
    button2v1a.pack()

def loadVentana1b():
    global ventanaPrincipal

    vaciarVentanaPrincipal()

    ventanaPrincipal.title("Manual")
    ventanaPrincipal.geometry("200x150")

    text1v1b = tk.Label(ventanaPrincipal, text= "Introduce la clave publica")
    text2v1b = tk.Label(ventanaPrincipal, text= "D:")
    input1v1b = tk.Entry(ventanaPrincipal)
    text3v1b = tk.Label(ventanaPrincipal, text= "N:")
    input2v1b = tk.Entry(ventanaPrincipal)
    button1v1b = tk.Button(ventanaPrincipal, text= "Continuar", command= lambda: funbutton1v1b(input1v1b.get(), input2v1b.get()))

    text1v1b.pack()
    text2v1b.pack()
    input1v1b.pack()
    text3v1b.pack()
    input2v1b.pack()
    button1v1b.pack()

def loadVentana2():
    global ventanaPrincipal

    vaciarVentanaPrincipal()

    ventanaPrincipal.title("Abrir mensage")
    ventanaPrincipal.geometry("750x100")

    text1v2 = tk.Label(ventanaPrincipal, text= "Seleccione el archivo del mensage")
    text2v2 = tk.Label(ventanaPrincipal, text= "Sin seleccionar")
    button1v2 = tk.Button(ventanaPrincipal, text= "Seleccionar archivo", command= lambda: text2v2.configure(text= funbutton1v2()))
    button2v2 = tk.Button(ventanaPrincipal, text= "Continuar", command= funbutton2v2)

    text1v2.pack()
    text2v2.pack()
    button1v2.pack()
    button2v2.pack()

def loadVentana3():
    global ventanaPrincipal
    global textoDesencriptado
    global textoEncriptado
    global d
    global n

    vaciarVentanaPrincipal()

    ventanaPrincipal.title("Desencriptando")
    ventanaPrincipal.geometry("150x100")

    text1v3 = tk.Label(ventanaPrincipal, text= "Desencriptando...")

    text1v3.pack()

    for caracterEncriptado in textoEncriptado:
        # Aplica la fórmula de encriptación RSA: (carácter^d) % n
        caracterDesencriptado = pow(caracterEncriptado, d, n)
        # Añade el carácter encriptado a la lista
        textoDesencriptado.append(caracterDesencriptado)

    loadVentana4()

def loadVentana4():
    global ventanaPrincipal

    vaciarVentanaPrincipal()

    ventanaPrincipal.title("Abrir mensage")
    ventanaPrincipal.geometry("750x100")

    text1v4 = tk.Label(ventanaPrincipal, text= "Seleccione donde guardar el archivo")
    text2v4 = tk.Label(ventanaPrincipal, text= "Sin seleccionar")
    button1v4 = tk.Button(ventanaPrincipal, text= "Seleccionar carpeta", command= lambda: text2v4.configure(text= funbutton1v4()))
    button2v4 = tk.Button(ventanaPrincipal, text= "Acabar", command= funbutton2v4)

    text1v4.pack()
    text2v4.pack()
    button1v4.pack()
    button2v4.pack()

def funbutton1v1a():
    global rutaClave

    rutaClave = filedialog.askopenfilename(
        title="Seleccionar un archivo de llave publica",
        filetypes=[("Archivos de texto", "*.txt"), ("Archivo de llave publica", "*.pub"), ("Todos los archivos", "*.*")]
    )

    return rutaClave

def funbutton2v1a():
    global d
    global n
    global rutaClave

    if (rutaClave.strip() != "") and (archivoExiste(rutaClave)):

        with open(rutaClave, 'r') as archivo:
            # Lee la primera línea del archivo y divide los valores "e" y "n"
            contenido = archivo.readline().split(", ")

            if len(contenido) == 2:
                d, n = contenido
            else:
                _, _, n, _, d = contenido
            # Convierte los valores "e" y "n" a enteros
            d = int(d)
            n = int(n)

        loadVentana2()

def funbutton1v1b(inD, inN):
    global d
    global n

    d = int(inD)
    n = int(inN)

    loadVentana2()

def funbutton1v2():
    global rutaAbrir

    rutaAbrir = filedialog.askopenfilename(
        title="Seleccionar un mensage para encriptar",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )

    return rutaAbrir

def funbutton2v2():
    global rutaAbrir
    global textoEncriptado

    if (rutaAbrir.strip() != "") and (rutaAbrir.endswith(".txt")) and (archivoExiste(rutaAbrir)):

        with open(rutaAbrir, 'r') as archivo:

            textoEncriptado = [int(num) for num in archivo.read().strip().split(", ")]

        loadVentana3()

def funbutton1v4():
    global rutaGuardar

    rutaGuardar = filedialog.askdirectory(title="Selecciona una carpeta para guardar el archivo")

    return rutaGuardar

def funbutton2v4():
    global rutaAbrir
    global rutaGuardar
    global textoDesencriptado

    if rutaGuardar.strip() != "":

        nombreArchivo = ""
        if rutaAbrir.split("/")[-1][-17:-4] == " - Encriptado":
            nombreArchivo = rutaAbrir.split("/")[-1][:-17]
        else:
            nombreArchivo = rutaAbrir.split("/")[-1][:-4]
        with open(rutaGuardar + "/" + nombreArchivo + " - Desencriptado" + ".txt", 'w') as archivo:
            archivo.write(''.join([chr(codigo) for codigo in textoDesencriptado]))

        cerrar()










# 3: Iniciar ventana principal

ventanaPrincipal = tk.Tk()
ventanaPrincipal.geometry("250x100")
ventanaPrincipal.title("Iniciando...")
text1v0 = tk.Label(ventanaPrincipal, text= "Iniciando...")
text1v0.pack(expand= True)










# 4: Variables

# Iniciar variables
n = 0
d = 0
rutaClave = ""
rutaAbrir = ""
rutaGuardar = ""
textoDesencriptado = []
textoEncriptado = []










# 5: Codigo

loadVentana1()










# 6: Mainloop ventana principal

ventanaPrincipal.mainloop()










# 7: Finalizar programa

exit()