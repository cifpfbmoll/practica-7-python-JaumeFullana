# Escribe un programa que lea una frase (entrada por teclado), y la pase como parámetro a un procedimiento.
# El procedimiento contará el número de vocales (de cada una) que aparecen, y lo imprimirá por pantalla.

def procedimiento (cadena):

    a=cadena.count("a")

    e=cadena.count("e")

    i=cadena.count("i")

    o=cadena.count("o")

    u=cadena.count("u")

    print (a+e+i+o+u)

frase=input("Escribe una frase:")

procedimiento(frase)