#Escribe un programa que lea (entrada por teclado) el nombre y los dos apellidos de una persona 
# (en tres cadenas de caracteres diferentes), los pase como parámetros a una función, y ésta debe unirlos 
# y devolver una única cadena. La cadena final la imprimirá el programa por pantalla.

def funcion(a,b,c):

    suma=a+b+c

    return suma

nombre=input("nombre:")

apellido1=input("Primer apellido:")

apellido2=input("Segundo apellido:")

print (funcion(nombre,apellido1,apellido2))


