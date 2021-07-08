#Escribe un programa que te pida una frase y una vocal (entrada por teclado), y pase estos datos como
#parámetro a una función que se encargará de cambiar todas las vocales de la frase por la vocal seleccionada.
#Devolverá la función la frase modificada, y el programa principal la imprimirá:

def funcion (cadena,cambio):

    nuevo=cadena.replace ("a",cambio)

    nuevo=nuevo.replace ("e",cambio)

    nuevo=nuevo.replace ("i",cambio)

    nuevo=nuevo.replace ("o",cambio)

    nuevo=nuevo.replace ("u",cambio)

    return nuevo

frase=input("Escribe una frase:")

vocal=input("Escribe una vocal:")

print (funcion(frase,vocal))