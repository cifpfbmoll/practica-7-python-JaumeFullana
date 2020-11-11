# Escribe un programa que pida un texto por pantalla, este texto lo pase como parámetro a un procedimiento,
# y éste lo imprima primero todo en minúsculas y luego todo en mayúsculas.

def procedimiento (cadena):

    print (cadena.lower ())
    
    print (cadena.upper ())

texto=input("Ecribe un texto:")

procedimiento(texto)