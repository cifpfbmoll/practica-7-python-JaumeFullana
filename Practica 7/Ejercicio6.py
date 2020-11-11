#Escribe un programa que lea el nombre de una persona y un carácter (entrada por teclado), 
# le pase estos datos a una función que comprobará si dicho carácter está en su nombre.
# El resultado de dicha función lo imprimirá el programa principal por pantalla.

def funcion (cadena,comprobar):

    resultado=cadena.rfind(comprobar)

    if resultado==-1:

        resultado=("Ese caracter no esta en tu nombre.")

    else:

        resultado=("Ese caracter esta en tu nombre.")

    return resultado

nombre=input("Escribe tu nombre:")

caracter=input("Escribe un caracter:")


print (funcion(nombre,caracter))