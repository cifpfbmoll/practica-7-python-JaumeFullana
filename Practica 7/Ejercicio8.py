# Escribe un programa que pida una frase (entrada por teclado), y pase la frase como parámetro a una 
# función que debe eliminar los espacios en blanco (compactar la frase). El programa principal imprimirá
# por pantalla el resultado final.

def funcion(cadena):

    sinespacios=cadena.replace(" ","")

    return sinespacios

frase=input("Escribe una frase:")

print (funcion(frase))


