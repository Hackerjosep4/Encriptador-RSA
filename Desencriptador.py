respuesta = ""
# Bucle que se ejecuta hasta que el usuario introduce "A" o "M"
while not respuesta in ["A", "M"]:
    # Imprime las opciones para introducir la clave privada
    print("Metodo para introducir clave privada:")
    print("\tA - Automatico")
    print("\tM - Manual")
    
    # Captura la respuesta del usuario, eliminando espacios y convirtiéndola a mayúsculas
    respuesta = input("Respuesta: ").strip().upper()
    print()

# Si la respuesta es "A" (Automático)
if respuesta == "A":
    # Solicita al usuario el nombre del archivo que contiene la clave privada
    nombreArchivoClave = input("Codigo del archivo de la clave (Clave_privada(codigo).txt): ").strip()
    
    # Abre el archivo con la clave privada en modo lectura
    with open(f"Clave_privada({nombreArchivoClave}).txt", 'r') as archivo:
        # Lee la primera línea del archivo y divide los valores, ignorando los dos primeros y el cuarto, extrayendo "n" y "d"
        _, _, n, _, d = archivo.readline().split(", ")
        # Convierte los valores "n" y "d" a enteros
        d = int(d)
        n = int(n)

# Si la respuesta es "M" (Manual)
else:
    # Solicita al usuario que introduzca manualmente los valores de "d" y "n"
    print("A continuacion introduce los numeros \"d\" y \"n\"")
    d = int(input("Numero d: ").strip())
    n = int(input("Numero n: ").strip())

print()

# Solicita al usuario el nombre del archivo que contiene el mensaje encriptado (sin la extensión .txt)
nombrearchivoMensage = input("Nombre del archivo (sin .txt): ").strip()
print()

# Abre el archivo que contiene el mensaje encriptado en modo lectura
with open(nombrearchivoMensage + ".txt", 'r') as archivo:
    # Lee el contenido del archivo, lo limpia y lo convierte en una lista de enteros
    textoEncriptado = archivo.read().strip().split(", ")
    textoEncriptado = [int(num) for num in textoEncriptado]

# Lista vacía donde se almacenarán los caracteres desencriptados
textoDesencriptado = []

# Bucle que recorre cada carácter encriptado
for caracterEncriptado in textoEncriptado:
    # Aplica la fórmula de desencriptación RSA: (carácter^d) % n
    caracterDesencriptado = (caracterEncriptado**d)%n
    # Añade el carácter desencriptado a la lista
    textoDesencriptado.append(caracterDesencriptado)

# Convierte la lista de códigos ASCII en una cadena de texto
texto = ''.join([chr(codigo) for codigo in textoDesencriptado])

# Si el nombre del archivo termina con " - Encriptado", se elimina esa parte del nombre
if nombrearchivoMensage.endswith(" - Encriptado"):
    nombrearchivoMensage = nombrearchivoMensage[:-13]

# Crea un nuevo archivo con el sufijo " - Desencriptado" y escribe el texto desencriptado en él
with open(nombrearchivoMensage + " - Desencriptado" + ".txt", 'w') as archivo:
    archivo.write(texto)

exit()