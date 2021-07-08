#Escribe un programa que pida una frase (entrada por teclado), y le pase como parámetro a una función dicha frase. 
#La función debe sustituir todos los espacios en blanco de una frase por un asterisco, y devolver el resultado 
#para que el programa principal la imprima por pantalla.

def funcion (cadena):

    cambio=cadena.replace (" ","*")

    return cambio

frase=input("Pon una frase:")

print (funcion(frase))