respuesta = ""
# Bucle que se ejecuta hasta que el usuario introduzca "A" o "M"
while not respuesta in ["A", "M"]:
    # Imprime las opciones de métodos para introducir la clave pública
    print("Metodo para introducir clave publica:")
    print("\tA - Automatico")
    print("\tM - Manual")
    
    # Toma la respuesta del usuario, eliminando espacios y convirtiéndola a mayúsculas
    respuesta = input("Respuesta: ").strip().upper()
    print()

# Si la respuesta es "A" (Automático)
if respuesta == "A":
    # Pide al usuario el nombre del archivo que contiene la clave pública
    nombreArchivoClave = input("Codigo del archivo de la clave (Clave_publica(codigo).txt): ").strip()
    
    # Abre el archivo con la clave pública en modo lectura
    with open(f"Clave_publica({nombreArchivoClave}).txt", 'r') as archivo:
        # Lee la primera línea del archivo y divide los valores "e" y "n"
        e, n = archivo.readline().split(", ")
        # Convierte los valores "e" y "n" a enteros
        e = int(e)
        n = int(n)

# Si la respuesta es "M" (Manual)
else:
    # Pide al usuario que introduzca los valores de "e" y "n"
    print("A continuacion introduce los numeros \"e\" y \"n\"")
    e = int(input("Numero e: ").strip())
    n = int(input("Numero n: ").strip())

print()

# Pide al usuario el nombre del archivo que contiene el mensaje a encriptar (sin la extensión .txt)
nombreArchivoMensage = input("Nombre del archivo del mensage (sin .txt): ").strip()
print()

# Abre el archivo que contiene el mensaje en modo lectura
with open(nombreArchivoMensage + ".txt", 'r') as archivo:
    # Lee el contenido del archivo, lo limpia y convierte cada carácter en su código ASCII
    textoDesencriptado = [ord(caracter) for caracter in archivo.read().strip()]

# Lista vacía donde se almacenarán los caracteres encriptados
textoEncriptado = []

# Bucle que recorre cada carácter desencriptado
for caracterDesencriptado in textoDesencriptado:
    # Aplica la fórmula de encriptación RSA: (carácter^e) % n
    caracterEncriptado = (caracterDesencriptado**e)%n
    # Añade el carácter encriptado a la lista
    textoEncriptado.append(caracterEncriptado)

# Convierte la lista de números encriptados en una cadena separada por comas
texto = ', '.join(str(numero) for numero in textoEncriptado)

# Crea un nuevo archivo con el sufijo " - Encriptado" y escribe el texto encriptado en él
with open(nombreArchivoMensage + " - Encriptado" + ".txt", 'w') as archivo:
    archivo.write(texto)

exit()