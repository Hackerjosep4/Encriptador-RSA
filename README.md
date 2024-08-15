# Encriptación RSA

Este proyecto consiste en un conjunto de scripts para generar claves RSA, encriptar y desencriptar mensajes utilizando el algoritmo RSA. Está diseñado para facilitar la comprensión y uso de la criptografía asimétrica en Python.

## Características

- **Generador de Claves RSA**: Genera pares de claves pública y privada con diferentes niveles de seguridad.
- **Encriptador**: Encripta mensajes utilizando una clave pública RSA.
- **Desencriptador**: Desencripta mensajes previamente encriptados utilizando la clave privada correspondiente.

## Archivos Principales

### 1. `Generador de claves.py`
Este script genera un par de claves RSA (una pública y una privada). El nivel de encriptado puede ajustarse según las necesidades del usuario (Prueba, Bajo, Medio, Alto). Las claves generadas se guardan en archivos de texto.

### 2. `Encriptador.py`
Este script encripta un mensaje utilizando una clave pública RSA. El mensaje debe estar guardado en un archivo de texto, y el resultado de la encriptación se guarda en un nuevo archivo de texto.

### 3. `Desencriptador.py`
Este script desencripta un mensaje previamente encriptado utilizando la clave privada RSA correspondiente. El mensaje desencriptado se guarda en un archivo de texto.

### 4. `Instalacion.bat`
Este archivo por lotes (`.bat`) automatiza la instalación de la dependencia `sympy`, necesaria para que los scripts funcionen correctamente. Al ejecutar este archivo, se instalará automáticamente la biblioteca utilizando `pip`.

## Requisitos

- Python 3.x
- Biblioteca `sympy` (si no está instalada, puedes instalarla manualmente o automáticamente con el archivo `Instalacion.bat`).

## Instalación

### Instalación Automática

1. Ejecuta el archivo `Instalacion.bat` haciendo doble clic sobre él.
2. Esto ejecutará el siguiente comando en la línea de comandos:
```pip install sympy```
Esto instalará la biblioteca `sympy` automáticamente.

### Instalación Manual

Si prefieres instalar la biblioteca manualmente, abre una terminal y ejecuta el siguiente comando:
```pip install sympy```


## Cómo utilizar

### 1. Generar Claves RSA
1. Ejecuta `Generador de claves.py`.
2. Selecciona el nivel de encriptado (Prueba, Bajo, Medio, Alto).
3. Introduce un código para la clave que se usará en los archivos de salida.
4. Las claves se guardarán en los archivos `Clave_publica(codigo).txt` y `Clave_privada(codigo).txt`.

### 2. Encriptar un Mensaje
1. Guarda el mensaje que deseas encriptar en un archivo de texto.
2. Ejecuta `Encriptador.py`.
3. Elige si deseas introducir la clave pública manualmente o cargarla desde un archivo.
4. Introduce el nombre del archivo que contiene el mensaje a encriptar.
5. El mensaje encriptado se guardará en un archivo de texto con el sufijo `- Encriptado`.

### 3. Desencriptar un Mensaje
1. Ejecuta `Desencriptador.py`.
2. Elige si deseas introducir la clave privada manualmente o cargarla desde un archivo.
3. Introduce el nombre del archivo que contiene el mensaje encriptado.
4. El mensaje desencriptado se guardará en un archivo de texto con el sufijo `- Desencriptado`.

## Contribución

Si deseas contribuir al desarrollo de este proyecto, ¡eres bienvenido! Puedes enviar pull requests con mejoras o correcciones de errores.

## Autor

Este proyecto fue creado por Hackerjosep4.

## Licencia

Este proyecto está bajo la licencia LICENSE.txt.