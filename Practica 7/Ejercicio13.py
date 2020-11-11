# Escribe un programa que le pida al usuario si quiere calcular si un número es primo con for o con while, 
# por tanto, habrá dos funciones que se caracterizan por hacer ese mismo cálculo de una manera (con for y sin breaks)
# , o de otra (con while). Ambas funciones devolverá true (si es primo) o false (si no es primo). 
# El programa principal informará del resultado. Además, como mejora puedes calcular el tiempo que tarda en encontrar 
# la solución de una manera u otra. Comentario: aprovecha el código que tienes ya creado

def funcionwhile (numero):

    if (numero==1):
    
        esprimo=False

    else:

        i=2
    
        while numero%i!=0:

            i+=1
    
        if i==numero:
    
            esprimo=True
    
        else:
    
            esprimo=False

    return esprimo

def funcionfor (numero):

    esprimo = True

    if (numero==1):
    
        esprimo=False

    else:
    
        for i in range (1,numero):
    
            if (i>1 and i<numero and numero%i==0):
        
                esprimo = False   

    return esprimo

import time

numero=int(input("Escribe un numero:"))

eleccion=input("Quieres saber si es primo con while o con for?")

esprimo=()

start_time = time.time()

if eleccion=="while":


    if funcionwhile(numero):

        print("El numero es primo")

        print("--- %s seconds ---" % (time.time() - start_time))

    else:

        print("El numero no es primo")

        print("--- %s seconds ---" % (time.time() - start_time))

elif eleccion=="for":

    
    if funcionfor(numero):

        print("El numero es primo")

        print("--- %s seconds ---" % (time.time() - start_time))

    else:

        print("El numero no es primo")

        print("--- %s seconds ---" % (time.time() - start_time))


else:

    print ("ERROR: Ese no es ninguno de los metodos posibles.")
