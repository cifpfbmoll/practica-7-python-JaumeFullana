# Escribe un programa que te pida una palabra o número, pase por parámetro estos datos a una función,
# y ésta te diga si es o no palíndroma o capicúa. El programa principal imprimirá el resultado de la función:

def funcion (cadena):

    alreves=("")

    for i in range(len(cadena)-1,-1,-1):
        
        alreves+=(cadena[i])
    
    if cadena == alreves:

        resultado=f"{cadena} es palindroma o capicua"

    else:

        resultado=f"{cadena} no es palindroma o capicua"

    return resultado

caracteres=input("Escribe una palabra o un numero:")

print (funcion(caracteres))

