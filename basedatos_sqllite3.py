
# CREAR BASE DE DATOS

import sqlite3
from sqlite3 import Error

def crearbase():

    try:
        con = sqlite3.connect('mibase.db')
        print("Base creada")
    except Error:
        print(Error)
    finally:
        con.close()

crearbase()

##############################################################################

# CREAR TABLA

import sqlite3
from sqlite3 import Error

def conectar():
    try:
        con = sqlite3.connect('mibase.db')
        return con
    except Error:

        print(Error)

def creartabla(con):

    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE personas(id integer PRIMARY KEY, nombre text, salario real)")
    con.commit()

con = conectar()

creartabla(con)

##############################################################################

# INSERTAR REGISTRO

import sqlite3
from sqlite3 import Error



def conectar():
    try:
        con = sqlite3.connect('mibase.db')
        return con
    except Error:

        print(Error)

def insertarregistro(con):

    cursorObj = con.cursor()

    cursorObj.execute("INSERT INTO personas VALUES(1, 'Juan', 700)")

    con.commit()

con = conectar()

insertarregistro(con)


##############################################################################

# ACTUALIZAR REGISTRO

import sqlite3
from sqlite3 import Error



def conectar():
    try:
        con = sqlite3.connect('mibase.db')
        return con
    except Error:

        print(Error)

def insertarregistro(con):

    cursorObj = con.cursor()

    cursorObj.execute('UPDATE personas SET nombre = "Pedro" where id = 1')
    con.commit()

con = conectar()

insertarregistro(con)


##############################################################################

# BORRAR REGISTRO

import sqlite3
from sqlite3 import Error



def conectar():
    try:
        con = sqlite3.connect('mibase.db')
        return con
    except Error:

        print(Error)

def insertarregistro(con):

    cursorObj = con.cursor()

    cursorObj.execute('DELETE from personas where id = 1')
    con.commit()

con = conectar()

insertarregistro(con)

##############################################################################



