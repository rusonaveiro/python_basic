# coding=utf-8
# EXPRESIONES REGULARES o REGEX
# Módulo re

"""
DOCUMENTACIÓN OFICIAL
https://docs.python.org/3.7/library/re.html
"""

"""
Las expresiones regulares nos permiten trabajar con textos, más específicamente para
realizar busquedas de texto a través de métodos y utilizando una sintaxis propia
de la librería de expresiones regulares que utilicemos en cada lenguaje. Normalmente
la sintaxis utilizada para los patrones de búsqueda es compartida por la mayoría de
los lenguajes de programación.

PODEMOS UTILIZAR EXPRESIONES REGULARES PARA:
- Saber si existe una cadena de caracteres (palabra) dentro de un texto
- Conocer cuantes veces se encuentra una cadena de caracteres dentro de un texto
- Detectar si un texto se ajusta a un formato específico por ejemplo un
correo electrónico "texto" "@" "texto" "." "com" "." "ar"
- etc...
"""

import re

# Clase 1 - re.search
# Este método nos buscará la primer coincidencia de una cadena de caracteres dentro de un texto
# devolverá un objeto si es localizado o None si no es encontrado.

cadena = "Hola estudiantes de AcademiaCoder. En AcademiaCoder los estudiantes aprenderan programación."

cadena2 = """
Hola estudiantes de AcademiaCoder.
En AcademiaCoder los estudiantes aprenderan programación.
Recuerden que nos centramos en el Desarrollo Web
"""

a_buscar = "estudiantes"

buscado = re.search(a_buscar, cadena)

"""
print(buscado)
print(buscado.start())
print(buscado.end())
print(buscado.span())
print(a_buscar)
"""
# Clase 2 - re.findall, re.split, re.sub
# En esta clase aprenderemos a utilizar estos métodos de la librería re
"""
re_findall = re.findall(a_buscar, cadena)  # Buscar estudiantes e imprime lista ['estudiantes', 'estudiantes']
print(re_findall)

re_split = re.split("\s", cadena)  # busca los espacios entre palabras
print(re_split)  # Imprime ['Hola', 'estudiantes', 'de', 'AcademiaCoder.', 'En', 'AcademiaCoder', 'los', 'estudiantes', 'aprenderan', 'programación.']

re_sub = re.sub(a_buscar, "desarrolladores", cadena)  # reemplaza palabra estudiante por desarrolladores
print(re_sub)  # imprime Hola desarrolladores de AcademiaCoder. En AcademiaCoder los desarrolladores aprenderan programación.


print(cadena2)
Impime:
Hola estudiantes de AcademiaCoder.
En AcademiaCoder los estudiantes aprenderan programación.
Recuerden que nos centramos en el Desarrollo Web

"""


# Clase 3 - Anclas y Metacaracteres (Sintaxis de RegEx)
# ^ (Caret), $, []
# El Caret se pone al pincipio para buscar palabras que comiencen con ese elemento, por ejemplo ^Marcos, nunca nos mostraria "Python - Marcos"
# El Dolar se pone al final para buscar palabras como por ejemplo todas las terminadas en mente como naturalmente, generalmente, etc
# [] conjunto de caracteres busca letras o palabras dentro de una cadena

lista = [
    "Marcos - Python",
    "Carlos - JavaScript",
    "Ana - JavaScript",
    "Marcos - PHP",
    "Natalia - Vue",
    "Violeta - Python",
    "Ana - Vue",
    "Carla - PHP",
    "Marcos - Programacion",
    "Benicio - Programación"
]

# Quitar las comillas triples para probar el código de la clase 3 de Expresiones regulares
"""
for linea in lista:
    if re.findall('Programaci[oó]n', linea):
        print(linea)

Imprime:
Marcos - Python
Marcos - PHP
Marcos - Programacion

"""

# Clase 4 - Rangos, Rango Negado, Clases Predefinidas, Cuantificadores y Otros Metacaracteres

# Rangos []

# [a-d] esto significaría que buscamos cualquier letra comprendida entre a y d es decir "abcd"


# [0-7] esto significaría que buscamos cualquier número comprendido entre 0 y 7 es decir "01234567"

# Rango Negado ^

cadena = "abcdef ghi" \
         "0123456789-"
# Clases Predefinidas

# \d corresponde a [0-9]
# \w todas las letras minus., mayus., números y guiones bajos
# \s corresponde a espacios en blanco (espacio, tabulaciones, nuevas lineas...)

"""
CUANTIFICADORES

Son caracteres que multiplican el patrón que les precede.
Mientras que con las clases de caracteres podemos buscar un dígito, o una letra; 
con los cuantificadores podemos buscar cero o más letras, al menos 7 dígitos, o entre tres y 
cinco letras mayúsculas. Los cuantificadores son:

?: coincide con cero o una ocurrencia del patrón. Dicho de otra forma, hace que el patrón sea opcional
+: coincide con una o más ocurrencias del patrón
*: coincide con cero o más ocurrencias del patrón.
{x}: coincide con exactamente x ocurrencias del patrón
{x, y}: coincide con al menos x y no más de y ocurrencias. Si se omite x, el mínimo es cero, y si se omite y, no hay máximo. Esto permite especificar a los otros como casos particulares: ? es {0,1}, + es {1,} y * es {,} o {0,}.
Ejemplos:

.* : cualquier cadena, de cualquier largo (incluyendo una cadena vacía)
[a-z]{3,6}: entre 3 y 6 letras minúsculas
\d{4,}: al menos 4 dígitos
.*[hH]ola!?: una cadena cualquiera, seguida de hola, y terminando (o no) con un !
"Mi nombre es Marcos, hola!"
"Mi nombre es Marcos, hola"
OTROS METACARACTERES
Existen otros metacaracteres en el lenguaje de las expresiones regulares:

?: Además de servir como cuantificador, puede modificar el comportamiento de otro. 
De forma predeterminada, un cuantificador coincide con la mayor cadena posible. 
Cuando se le coloca un ?, se indica que se debe coincidir con la menor cadena posible. 
Esto es: dada la cadena bbbbb, b+ coincide con la cadena entera, mientras que b+? coincide solamente con b. 
Es decir, la menor cadena que cumple el patrón.

(): agrupan patrones. Sirven para que aquel pedazo de la cadena que coincida con el patrón sea capturado; 
o para delimitar el alcance de un cuantificador. Ejemplo: ab+ coincide con ab, abb, abbbbb, …, 
mientras que (ab)+ coincide con ab, abab, abab…

| : permite definir opciones para el patrón: perro|gato coincide con perro y con gato.
"""

#########################################################################################################

# compile(): Para tomar la expresión regular, la cual en este caso es ‘p+’
# match(): Para comparar la expresión regular con el string sobre el cual estamos buscando.

import re

patron = re.compile('[p+]')
lista = ['pera', 'vfg']

print(patron.match(lista[0]))
print(patron.match(lista[1]))

if (patron.match(lista[1])!='None'):
    print('no validado')

#########################################################################################################

# Caracteres, clases y rangos

import re

patron = re.compile('pera''|manzana')
string = "manzana"

print(patron.match(string))

#########################################################################################################

# Sub-patrones – ( )

import re

patron = re.compile('(?i)pera|manzana')
string = "MANZANA"

print(patron.match(string))

#########################################################################################################

# (?:...)

import re
# #############################################
# Forma 1
# #############################################
patron = re.compile(r'(?i:pera) y manzana')
string1 = "pera y manzana"
string2 = "PERA y manzana"
string3 = "Pera y manzana"
string4 = "PERA Y manzana"
print(patron.match(string1))
print(patron.match(string2))
print(patron.match(string3))
print(patron.match(string4))

# #############################################
# Forma 2
# #############################################
m = re.search('(?i:abc)def', 'Abcdef')
print(m.group(0))

print('---'*23)
# #############################################
# Forma 3
# #############################################
patron2 = '(?i:pera) y manzana'
string5 = "pera y manzana"
string6 = "PERA y manzana"
string7 = "Pera y manzana"
string8 = "PERA Y manzana"
print(re.match(patron2, string5))
print(re.match(patron2, string6))
print(re.match(patron2, string7))
print(re.match(patron2, string8))

#########################################################################################################

# (?P<nombre>...)

import re

patron = re.compile(r'(?P<etiqueta>[A-Z][A-Z0-9]*)\b[^>]*>.*?</(?P=etiqueta)')
string1 = "Prueba <B><I>Texto en negrita e italica</I></B> Esto solo es texto."

print(patron.search(string1))


"""
'B><I>Texto en negrita e italica</I></B'>
"""

#########################################################################################################

# (?=...)

import re

patron = re.compile(r'color (?=rojo)')
string1 = "El auto de color rojo."

print(patron.search(string1))

#########################################################################################################

# (?=!...)

import re

patron = re.compile(r'color (?!rojo)')
string1 = "El auto de color azul."

print(patron.search(string1))

#########################################################################################################

# Búsqueda hacia atrás (?<= (?<!

import re

patron = re.compile(r'(?<=color )azul')
string1 = "El auto de color azul."

print(patron.search(string1))

m = re.search(r'(?<=color )azul', 'El auto de color azul.')
print(m.group(0))

#########################################################################################################

# Condicional

import re
patron1 = re.compile(r'((?P<name>ap8)(?(name)9|))')

mail = 'ap89 ap8 rp8 rp4 w'
print(patron1.search(mail))

patron2 = re.compile(r'(<)?(\w+@\w+(?i:\.\w+)+)(?(1)>|$)')
mail1 = "<user@host.com>"
mail2 = "user@host.com"
mail3 = "<user@Host.com"
mail4 = "user@host.com>"
print(patron2.search(mail1))
print(patron2.search(mail2))
print(patron2.search(mail3))
print(patron2.search(mail4))

#########################################################################################################

# Descripción del módulo.

import re
patron1 = re.compile(r'(<)?(\w+@\w+(?:\.[a-z]+)+)(?(1)>|$)', re.I)

mail = "<user@host.Com>"
print(patron1.search(mail))

patron2 = re.compile(r'(<)?(\w+@\w+(?i:\.[a-z]+)+)(?(1)>|$)')
mail1 = "<user@host.Com>"
print(patron2.search(mail1))

###############

# De igual forma podemos utilizar re.A, re.I, re.L, re.M y re.X

import re
patron1 = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)

mail = "3.3"
print(patron1.search(mail))

#########################################################################################################

# re.search (patrón, cadena, banderas = 0)

import re
patron1 = re.search(r'un.','Hola esto es una prueba, se escribe de nuevo un hola', flags=0)

print(patron1)

#########################################################################################################

# re.split()
# re.split(patrón, cadena, maxsplit=0, banderas = 0)

import re
retorno1 = re.split(r'\W+', 'Palabras, palabras, palabras.')
retorno2 = re.split(r'(\W+)', 'Palabras, palabras, palabras.')
retorno3 = re.split(r'\W+', 'Palabras, palabras, palabras.', 1)
retorno4 = re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
retorno5 = re.split('[a-f]+', '0a3B9')
print(retorno1)
print(retorno2)
print(retorno3)
print(retorno4)
print(retorno5)
print("----------------------------")
retorno5 = re.split(r'\W+', '...Palabras..., palabras, palabras...')
retorno6 = re.split(r'(\W+)', '...Palabras..., palabras, palabras...')
print(retorno5)
print(retorno6)

#########################################################################################################

# re.findall()
# re.findall(patrón, cadena, banderas = 0)

#########################################################################################################
