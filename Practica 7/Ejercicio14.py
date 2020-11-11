# Aprovechando el potencial de los diccionarios, escribe un programa que llame a un procedimiento,
# que recibe como parámetro la fecha en números y devuelve la fecha  con el nombre del mes.
# Comentario: no es necesario validar si la fecha es correcta, damos por hecho que lo será. 

def procedimiento (fecha):

    mes=fecha[3:5]

    enletras=diccionario[mes]

    fechaletras=fecha[0:2]+" de "+enletras+" de "+fecha[6:10]

    return fechaletras

diccionario = {"01":"Enero",
"02":"Febrero",
"03":"Marzo",
"04":"Abril",
"05":"Mayo",
"06":"Junio",
"07":"Julio",
"08":"Agosto",
"09":"Septiembre",
"10":"Octubre",
"11":"Noviembre",
"12":"Diciembre"
}

fecha=input("Escribe una fecha en numeros:")

print (procedimiento(fecha))

