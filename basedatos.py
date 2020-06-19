# instalar en Terminal: pip3 install mysql-connector
# importar en Python3: import mysql.connector
# instalar MAMP: preferencias -> Set Web & MySQL ports to 80 & 3306 -> ok
# luego de crear programa ir a MAMP -> Open WebStart page -> Tools -> PHPMyAdmin

######################################################################################

# Crear Base de Datos con "CREATE DATABASE mi_plantilla2"

import mysql.connector

config = {
  'user': 'root',
  'password': 'root',
  'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
  'raise_on_warnings': True,
}

link = mysql.connector.connect(**config)

if link.is_connected:
    print('Connection successfully established!')

cursor = link.cursor()
cursor.execute("CREATE DATABASE mi_plantilla2")

print("Despues de 25hs investigando logre la conexion con la base de datos")

######################################################################################

# Crear Tabla con "CREATE TABLE producto( id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, titulo bla bla bla

import mysql.connector
mibase = mysql.connector.connect(
    user="root",
    passwd="root",
    unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock",
    raise_on_warnings=True,
    database="mi_plantilla2"  # aqui agrego la db creada en el paso anterior
)
micursor = mibase.cursor()
micursor.execute("CREATE TABLE producto( id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, titulo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, ruta varchar(128) COLLATE utf8_spanish2_ci NOT NULL, descripcion text COLLATE utf8_spanish2_ci NOT NULL )")

######################################################################################

# Insertar Registros con "INSERT INTO producto(bla, bla, bla) VALUES(%s, %s, %s)"

import mysql.connector
mibase = mysql.connector.connect(
    user="root",
    passwd="root",
    unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock",
    raise_on_warnings=True,
    database="mi_plantilla2"
)
micursor = mibase.cursor()

sql = "INSERT INTO producto(titulo, ruta, descripcion) VALUES(%s, %s, %s)"
datos = ("Tema3", "ruta3", "descripcion 3")

micursor.execute(sql, datos)
mibase.commit()

# Para pasar varios datos como una lista de tupla, usaria .executemany
# datos = [("Tema4", "ruta4", "descripcion 4"), ("Tema5", "ruta5", "descripcion 5"), ("Tema6", "ruta6", "descripcion6")]
# micursor.executemany(sql, datos)

######################################################################################

# Borrar Registro con "DELETE FROM producto WHERE id=%s"

import mysql.connector
mibase = mysql.connector.connect(
    user="root",
    passwd="root",
    unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock",
    raise_on_warnings=True,
    database="mi_plantilla2"
)
micursor = mibase.cursor()

sql = "DELETE FROM producto WHERE id=%s"
dato = ('2',)

micursor.execute(sql, dato)

mibase.commit()

print(micursor.rowcount, "Registro borrado")

######################################################################################

# Seleccionar registros con "SELECT * FROM producto"

import mysql.connector
mibase = mysql.connector.connect(
    user="root",
    passwd="root",
    unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock",
    raise_on_warnings=True,
    database="mi_plantilla2"
)
micursor = mibase.cursor()

sql = "SELECT * FROM producto"

micursor.execute(sql)
resultado = micursor.fetchall()  # lista de tuplas insertadas y su Id

for x in resultado:  # recorre los 3 registros que creamos (lista) y luego los imprime en forma de tuplas con su numero de Id
    print(x)

""" Imprime:
(1, 'Tema3', 'ruta3', 'descripcion 3')
(3, 'Tema5', 'ruta5', 'descripcion 5')
(4, 'Tema6', 'ruta6', 'descripcion6')
"""

######################################################################################

# Actualizar Registro con "UPDATE producto SET titulo = 'Titulo 8' WHERE titulo = 'Tema 3'"

import mysql.connector as sql
base = sql.connect(
    user='root',
    passwd='root',
    database='mi_plantilla2',
    unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock',
    raise_on_warnings=True
)
cursor = base.cursor()
sql = "UPDATE producto SET titulo = 'Titulo 8' WHERE titulo = 'Tema 3'"

cursor.execute(sql)
base.commit()
print(cursor.rowcount, "Cantidad de registros afectados")

######################################################################################

# Comandos
"""
Un cursor es como un identificador de archivo que podemos usar para realizar operaciones 
en los datos almacenados en la base de datos. Llamar a cursor() es muy similar 
conceptualmente a llamar a open() cuando se trata de archivos de texto.
"""
cursor.execute('DROP TABLE IF EXISTS Tracks')  # elimina la tabla Tracks de la base de datos si existe. Este patrón es simplemente para permitirnos ejecutar el mismo programa para crear la tabla Tracks una y otra vez sin causar un error.
cursor.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')  # crea una tabla llamada Tracks con una columna de texto llamada title y una columna entera llamada plays.
cursor.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Thunderstruck', 20))  # INSERT indica qué tabla estamos usando y luego define una nueva fila al enumerar los campos que queremos incluir (título, jugadas) seguido de los VALORES
cursor.execute('SELECT * FROM Tracks WHERE title = 'My Way')  # La declaración SELECT te permite especificar qué columnas deseas recuperar, así como una cláusula WHERE para seleccionar qué filas deseas ver.
cursor.execute('SELECT title,plays FROM Tracks ORDER BY title)  # Puedes solicitar que las filas devueltas se ordenen por uno de los campos
cursor.execute('DELETE FROM Tracks WHERE title = 'My Way')  # Para eliminar una fila, necesitas una cláusula WHERE en una sentencia SQL DELETE. La cláusula WHERE determina qué filas se van a eliminar
cursor.execute('UPDATE Tracks SET plays = 16 WHERE title = 'My Way')  # Es posible UPDATE una columna o columnas dentro de una o más filas en una tabla
commit()  # para forzar que los datos se escriban en el archivo de la base de datos.
cursor.fetchone()  # obtener una tupla
cursor.fetchall()  # obtener muchas tuplas
cursor.close()

######################################################################################








