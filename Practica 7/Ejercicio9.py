# Escribe un programa que pida dos palabras las pase como parámetro a un procedimiento y diga si riman
# o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden solo las dos 
# últimas tiene que decir que riman un poco y si no, que no riman.

def procedimiento (cadena1,cadena2):

    riman=cadena1[-3:].endswith(cadena2[-3:])

    rimanpoco=cadena1[-2:].endswith(cadena2[-2:])

    if riman:

        print ("Las palabras",cadena1,"y",cadena2,"riman")

    elif rimanpoco:

        print ("Las palabras",cadena1,"y",cadena2,"riman un poco")

    else:

        print ("Las palabras",cadena1,"y",cadena2,"no riman")

palabra1=input("Escribe una palabra:")

palabra2=input("Escribe otra palabra:")

procedimiento(palabra1,palabra2)
