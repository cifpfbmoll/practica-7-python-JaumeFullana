# Escribe un programa que te pida una frase, y pase la frase como parámetro a una función. 
# Ésta debe devolver si es palíndroma o no, y el programa principal escribirá el resultado por pantalla:

def funcion (cadena):

    sinespacios=cadena.replace(" ","")

    alreves=("")

    for i in range(len(sinespacios)-1,-1,-1):
        
        alreves+=(sinespacios[i])
    
    if sinespacios == alreves:

        resultado=f"{cadena} es palindroma"

    else:

        resultado=f"{cadena} no es palindroma"

    return resultado

frase=input("Escribe una frase:")

print (funcion(frase))


