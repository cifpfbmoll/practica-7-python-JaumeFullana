# Escribe un programa que lea (entrada por teclado) una frase, y la pase como parámetro a un procedimiento, 
# y éste debe mostrar la frase con un carácter en cada línea.

def procedimiento (cadena):

    for i in cadena:

        print (i)

frase=input("ponga una frase:")

procedimiento(frase)