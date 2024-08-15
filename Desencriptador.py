respuesta = ""
while not respuesta in ["A", "M"]:
    print("Metodo para introducir clave privada:")
    print("\tA - Automatico")
    print("\tM - Manual")
    respuesta = input("Respuesta: ").strip().upper()
    print()

if respuesta == "A":
    nombreArchivoClave = input("Codigo del archivo de la clave (Clave_privada(codigo).txt): ").strip()
    with open(f"Clave_privada({nombreArchivoClave}).txt", 'r') as archivo:
        _, _, n, _, d = archivo.readline().split(", ")
        d = int(d)
        n = int(n)

else:
    print("A continuacion introduce los numeros \"d\" y \"n\"")
    d = int(input("Numero d: ").strip())
    n = int(input("Numero n: ").strip())

print()
nombrearchivoMensage = input("Nombre del archivo (sin .txt): ").strip()
print()

with open(nombrearchivoMensage + ".txt", 'r') as archivo:
    textoEncriptado = archivo.read().strip().split(", ")
    textoEncriptado = [int(num) for num in textoEncriptado]

textoDesencriptado = []

for caracterEncriptado in textoEncriptado:
    caracterDesencriptado = (caracterEncriptado**d)%n
    textoDesencriptado.append(caracterDesencriptado)

texto = ''.join([chr(codigo) for codigo in textoDesencriptado])

if nombrearchivoMensage.endswith(" - Encriptado"):
    nombrearchivoMensage = nombrearchivoMensage[:-13]

with open(nombrearchivoMensage + " - Desencriptado" + ".txt", 'w') as archivo:
    archivo.write(texto)