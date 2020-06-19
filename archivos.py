# ARCHIVOS (de texto)

# Abrir y Cerrar archivos

archivo_estudiantes = open("estudiantes.txt", "a")  # Así abrimos un archivo
print(archivo_estudiantes.write("\nCarolina Massutti - ReactJS"))
archivo_estudiantes.close()  # Así cerramos un archivo

# Eliminar un archivo
import os

os.remove("estudiantes2.txt")


output = open(r’C:\span’, ‘w’)  # Crea un archivo de salida (‘w’ significa escritura)
input = open('data', 'r')  # Crea un archivo de entrada (‘r’ significa lectura)
aString = input.read()  # Lee el archivo como si fuera un string.
aString = input.read(N)  # Lee hasta los siguientes N caracteres (o bytes) en un string.
aString = input.readline()  # Lea la siguiente línea (incluyendo \ n nueva línea) en una cadena
aList = input.readlines()  # Lea el archivo completo en una lista de líneas de string (con \ n)
output.write(aString)  # Escribe una cadena de caracteres (o bytes) en el archivo
output.writelines(aList)  # Escribe todas las cadenas de líneas en una lista en un archivo
output.close()  # Cierre manual
output.flush()  # Vaciar el búfer de salida al disco sin cerrar
for line in open('data'):  # use line Los iteradores de archivos leen línea por línea
open('f.txt', encoding='latin-1')  # Archivos de texto Python 3.X Unicode (cadenas de caracteres)
open('f.bin', 'rb')  # Archivos de bytes Python 3.X (cadenas de bytes)

##########################################################

# Crear y escribir en archivo
archivo = open('archivo1.txt', 'w')
archivo.write('Texto agregado desde script\n')
archivo.close()



# Leer archivo
"""
Creo un archivo de texto que se llama archivo2.txt
tele
mouse
ipad
remoto
mac
"""

archivo = open('archivo2.txt', 'r', encoding='utf-8')  # Hemos establecido que vamos a leer información del archivo mediante el uso del parámetro ‘r’,
print('------- Imprimo líneas en lista -------')       # Determinamos que el código que vamos a leer se encuentra en español mediante el parámetro (encoding='utf-8').
print(archivo.readlines(), end='\n')  # guardando cada línea con su salto de línea dentro de los elementos de una lista
print('------- Imprimo líneas -------')
archivo.seek(0)
for x in archivo:
    print(x, end='')  # método seeck(0) para pararnos en la primera línea y mediante el bucle “for” imprimimos línea por línea.
archivo.close()

""" Imprime
------- Imprimo líneas en lista -------
['tele\n', 'mouse\n', 'ipad\n', 'remoto\n', 'mac\n', '\n']
------- Imprimo líneas -------
tele
mouse
ipad
remoto
mac
"""

# Opciones de apertura de archivos
‘r’  # Abre un archivo para lectura.
‘w’  # Abre un archivo para escritura, si el archivo no existe lo crea.
‘x’  # Crea y abre un archivo, si éste ya existe la operación falla.
‘a’  # Abre un archivo para agregar al final del mismo sin truncar, si el archivo no existe lo crea.
‘t’  # Abre en modo texto.
‘b’  # Abre en modo binario.
‘+’  # Abre un archivo para actualizar (leer y escribir)


































