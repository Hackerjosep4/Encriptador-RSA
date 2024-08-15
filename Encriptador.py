respuesta = ""
while not respuesta in ["A", "M"]:
    print("Metodo para introducir clave publica:")
    print("\tA - Automatico")
    print("\tM - Manual")
    respuesta = input("Respuesta: ").strip().upper()
    print()

if respuesta == "A":
    nombreArchivoClave = input("Codigo del archivo de la clave (Clave_publica(codigo).txt): ").strip()
    with open(f"Clave_publica({nombreArchivoClave}).txt", 'r') as archivo:
        e, n = archivo.readline().split(", ")
        e = int(e)
        n = int(n)

else:
    print("A continuacion introduce los numeros \"e\" y \"n\"")
    e = int(input("Numero e: ").strip())
    n = int(input("Numero n: ").strip())

print()
nombreArchivoMensage = input("Nombre del archivo del mensage (sin .txt): ").strip()
print()

with open(nombreArchivoMensage + ".txt", 'r') as archivo:
    textoDesencriptado = [ord(caracter) for caracter in archivo.read().strip()]

textoEncriptado = []

for caracterDesencriptado in textoDesencriptado:
    caracterEncriptado = (caracterDesencriptado**e)%n
    textoEncriptado.append(caracterEncriptado)

texto = ', '.join(str(numero) for numero in textoEncriptado)

with open(nombreArchivoMensage + " - Encriptado" + ".txt", 'w') as archivo:
    archivo.write(texto)