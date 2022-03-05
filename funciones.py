import sys
import MySQLdb
from datetime import datetime, timedelta

#Conectar a base de datos 

def Conectar_BD(host,usuario,password,nombrebd):
    try:
        db = MySQLdb.connect(host,usuario,password,nombrebd)
        return db
    except MySQLdb.Error as e:
        print("No puedo conectar a la base de datos:",e)
        sys.exit(1)

#Desconectar base de datos

def Desconectar_BD(db):
    db.close()

#Menú

def MostrarMenu():
    menu='''
    1. Listar todos los campeones con sus apodos indicando el número de campeones
    2. Buscar Campeón en concreto y mostrar su clase
    3. Mostrar Campeón que tenga la misma velocidad que el número introducido
    4. Insertar nuevo campeón con todos su datos y sus respectivas estadísticas
    5. Borrar un campeón cuyo nombre sea pedido en el programa
    6. Actualizar fecha de creación de un campeón en concreto
    0. Salir
    '''
    print(menu)
    while True:
        try:
            opcion=int(input("Opción:"))
            return opcion
        except:
            print("Opción incorrecta, debe ser un número")

#Listar campeones y apodos


def listar_campeones(db):
    sql="select name,title from campeon"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
       cursor.execute(sql)
       registros = cursor.fetchall()
       return registros
    except:
       print("Error en la consulta")

#Contar campeones

def contar_campeones(db):
    sql="select * from campeon"
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    try:
       cursor.execute(sql)
       return cursor.rowcount
    except:
        print("Error en la consulta")

#Bucar campeón y mostrar su clase
def ver_clase(db,nombre):
    sql="select clase from campeon where name='%s';" %nombre
    cursor=db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        registros=cursor.fetchall()
        return registros
    except:
        print("Error en la consulta")


#Mostrar Campeón que tenga la misma velovidad que el número introducido

def campeon_velocidad(db,velocidad):
    sql="select name from campeon where id in(select id from estadistica where velocidad=%d);"%velocidad
    cursor=db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        registros=cursor.fetchall()
        return registros
        #for campeon in registros:
            #print(campeon.get("name"))
    except:
        print("Error en la consulta")

#Insertar campeón

def insertar_campeon(db,campeon):
    cursor=db.cursor()
    sql="insert into campeon(id,name,fecha_creacion,title,clase) values('%s','%s','%s','%s','%s');"%(campeon.get("id"),campeon.get("name"),campeon.get("fecha_creacion"),campeon.get("title"),campeon.get("clase"))
    try:
        cursor.execute(sql)
        db.commit()
        print("Campeón añadido con éxito")
    except:
        print("Error al insertar al campeón")
        db.rollback

#Insertar estadisticas

def insertar_estadistica(db,estadistica):
    cursor=db.cursor()
    sql="insert into estadistica(id,codigo,vida,velocidad,armadura,daño) values('%s',%i,%i,%i,%i,%i);"%(estadistica.get("id"),estadistica.get("codigo"),estadistica.get("vida"),estadistica.get("velocidad"),estadistica.get("armadura"),estadistica.get("daño"))
    try:
        cursor.execute(sql)
        db.commit()
        print("Estadisticas añadidas con exito")
    except:
        print("Error al insertar las estadisticas")
        db.rollback

#Borrar campeón 
def borrar_campeon(db,nombre):
    sql="delete from campeon where id='%s'"%nombre
    cursor=db.cursor()
    pregunta=input("¿Quieres borrar el campeón? S/N")
    if pregunta=="s" or pregunta=="S":
        try:
            cursor.execute(sql)
            db.commit()
            print("Campeón borrado con éxito")
            if cursor.rowcount==0:
                print("No existen campeones con ese nombre")
        except:
            print("Error al borrar")
            db.rollback()


#Borrar estadisticas del campeón
def borrar_estadisticas(db,nombre):
    sql="delete from estadistica where id='%s'"%nombre
    cursor=db.cursor()
    pregunta=input("¿Quieres borrar las estadisticas del campeón? S/N")
    if pregunta=="s" or pregunta=="S":
        try:
            cursor.execute(sql)
            db.commit()
            print("Estadisticas borradas con éxito")
            if cursor.rowcount==0:
                print("El campeón no tenía estadisticas registradas")
        except:
            print("Error al borrar")
            db.rollback()

#Actualizar fecha de creación

def actualizar_fecha(db,fecha,nombre):
    cursor=db.cursor()
    sql="update campeon set fecha_creacion='%s' where name='%s'"%(fecha,nombre)
    try:
        cursor.execute(sql)
        db.commit()
        print("Fecha de creación actualizada con éxito")
    except:
        print("Error al actualizar")
        db.rollback()



