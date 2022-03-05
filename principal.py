from funciones import *
import time

db = Conectar_BD("localhost","proyectobd","proyectobd","proyecto")

opcion=MostrarMenu()
while opcion!=0:
    if opcion==1:
        for campeon in listar_campeones(db):
            print("Nombre:",campeon.get("name"))
            print("Apodo:",campeon.get("title"))
        print ("Número total de campeones registrados:",contar_campeones(db))
        time.sleep(3)
    if opcion==2:
        nombre=str(input("Escribe nombre del campeón: "))
        if len(ver_clase(db,nombre)) != 0:
            for campeon in ver_clase(db,nombre):
                print(campeon.get("clase"))
        else:
            print("El campeón introducido no existe")
        time.sleep(2)
    if opcion==3:
        velocidad=int(input("Indica velocidad: "))
        if len(campeon_velocidad(db,velocidad)) != 0:    
            for campeon in campeon_velocidad(db,velocidad):
                print(campeon.get("name"))
        else:
            print("No existen campeones con esa velocidad")
        time.sleep(2)
    if opcion==4:
        campeon={}
        campeon["id"]=input("ID: ")
        campeon["name"]=input("Nombre del campeón: ")
        campeon["fecha_creacion"]=input("Introduce la fecha de creación del campeón [yyy-mm-dd]: ")
        campeon["title"]=input("Introduce el apodo del nuevo campeón: ")
        campeon["clase"]=input("Introduce la clase del nuevo campeón [Marksman, Tank, Assasin, Figther, Support, Mage]:")
        insertar_campeon(db,campeon)
        time.sleep(2)
        print("-Ahora Introduce las estadisticas del campeón-")
        estadistica={}
        estadistica["id"]=campeon.get("id")
        estadistica["codigo"]=int(input("Introduce el código: "))
        estadistica["vida"]=int(input("Introduce vida de %s: "%campeon.get("name")))
        estadistica["velocidad"]=int(input("Introduce velocidad de %s: "%campeon.get("name")))
        estadistica["armadura"]=int(input("Introduce armadura de %s: "%campeon.get("name")))
        estadistica["daño"]=int(input("Introduce daño de %s: "%campeon.get("name")))
        insertar_estadistica(db,estadistica)
        time.sleep(2)
    if opcion == 5:
        campeon=input("Introduce el nombre del campeón que quieras borrar: ")
        nombre=campeon.lower()
        borrar_campeon(db,nombre)
        borrar_estadisticas(db,nombre)
        time.sleep(2)
    if opcion ==6:
        nombre=input("Introduce el nombre del campéon al cual le quieres actualizar la fecha de creación: ")
        fecha=input("Introduce la nueva fecha de creación [yyyy-mm-dd]: ")
        actualizar_fecha(db,fecha,nombre)
        time.sleep(2)
    else:
        print("Opción incorrecta.")
    opcion=MostrarMenu()
Desconectar_BD(db)
