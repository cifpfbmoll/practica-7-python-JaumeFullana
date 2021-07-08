# Desarrolla un programa que nos sirva para gestionar nuestros contactos (la información a gestionar será el teléfono,
#  nombre, apellido1, apellido2 y correo electrónico. El programa tendrá un menú, con las siguientes opciones: añadir contacto,
#  consultar contacto a partir de la clave, consultar todos los contactos y eliminar contacto. Aprovecha lo que has aprendido
#  hasta el momento (diccionarios, funciones, procedimientos…).


def funciondel (eliminar):
    
    if eliminar in contactos:

        print (contactos.pop(eliminar),"ha sido eliminado.")

        respuesta=input("Desea hacer algo mas?")

    else:

        print (eliminar, "no es un numero de telefono de los contactos guardados.")

        respuesta=input("Desea hacer algo mas?")
        
    return respuesta

def procedimientoañadir ():

    telefono=input("Escribe su numero de telefono:")

    nombre=input("Escribe su nombre:")

    apellido1=" "+input("Escribe su primer apellido:")

    apellido2=" "+input("Escribe su segundo apellido:")

    correo=" "+input("Escribe su correo electronico:")

    informacion=nombre+apellido1+apellido2+correo

    contactos.setdefault(telefono, informacion)

print ("Bienvenido al programa de gestion de contactos! En este programa puede añadir, consultaro y eliminar contactos!\n\
Para añadir un contacto escriba: añadir \n\
Para consultar un contacto escriba: consultar\n\
Para consultar todos los contactos escriba: todos\n\
Para eliminar un contacto escriba: eliminar\n\
Para terminar el programa escriba: terminar")

contactos = dict()

respuesta=input("Que desea hacer?")

while respuesta != "terminar":

    if respuesta == "añadir":

        procedimientoañadir()

        respuesta=input("Desea hacer algo mas?")


    elif respuesta == "consultar":

        consulta=input("Escriba el numero de telefono que quiere consultar:")

        print (contactos[consulta])

        respuesta=input("Desea hacer algo mas?")


    elif respuesta == "todos":

        for k,v in contactos.items():
        
            print (k,":",v)


        respuesta=input("Desea hacer algo mas?")


    elif respuesta == "eliminar":

        eliminar=input("Pon el numero de telefono del contacto que quieres eliminar:")

        respuesta=funciondel(eliminar)

    else:

        respuesta=input("El comando introducido es incorrecto, introduzca un comando valido:")


print ("Hasta la proxima!")