'''
1) Desarrollar una función que reciba como parámetro el nombre y edad de una persona,
    retorne un String que indique si la persona es mayor de edad o menor de edad
    Ejemplo:
        'Pedro Perez es mayor de edad'
        ó 'Pedro Perez es menor de edad'

2) Desarrollar una función que retorne un String con una serie de ejercicios al usuario, 
la función debe recibir como parámetro un String.
    facil:
        "10 flexiones de pecho
        10 sentadillas"
    medio:
        "50 flexiones de pecho
        10 burpes
        50 sentadillas"
    avanzado:
        "100 flexiones de pecho con palmada
        80 paracaidistas
        200 abdomilaes"
    NOTA:
        \n -> Salto de linea
        \t -> Tabular
'''

def indicar_mayor_de_edad(usuario: str, edad: int):
    cadena = ''
    if edad >= 18:
        cadena = f'{usuario} es mayor de edad'
    else:
        cadena = f'{usuario} es menor de edad'
    return cadena

#Solución de Juan José
def ejercicios(a: str):
    if a == "facil":
        s="10 flexiones de pecho \t 10 sentadillas"
    elif a == "medio":
        s="50 flesiones de pecho \t 10 burpes \t 50 sentadillas"
    elif a == "avanzado":
        s="100 flexiones de pecho con palmada \t 80 paracaidistas \t 200 abdominales"
    else:
        s="No ingresó nivel de dificutad"
    return s

'''

3) Desarrollar una función que retorne una cadena con el valor del interes y 
el total del dinero a retirar de un CDT.
    * Si el usuario retira el dinero menor o igual a dos meses se 
        aplica una penalidad del 2%(0.02) y por lo tanto no generaría interés.
            *valor_penalidad = dinero_invertido * 0.02
    *Si el usuario retira el dinero mayor a dos meses recibirá un interés sobre su dinero
        valor_interes = (dinero * porcentaje_interes * tiempo) / 12
    
    NOTA:
        La función deberá recibir como parámetro: dinero, porcentaje_interes, tiempo
    
    Ejemplo de la cadena que debe retornar si no aplica penalidad:
        "*El valor del interés es de {valor_interes} 
         *El total del dinero a retirar es {total_dinero}"
    Si aplica penalidad:
        "*El valor de la penalidad es de {valor_penalidad}
        *El total del dinero a retirar es {total_dinero}"

'''

#Solución del punto 3
#Cristian Fabian
def valInt(dinero, porcentaje_interes, tiempo):
    if tiempo <= 2:
        valor_penalidad = dinero * 0.02
        total_dinero = dinero-valor_penalidad
        return f"*El valor de la penalidad es de {valor_penalidad}\n*El total del dinero a retirar es {total_dinero}"

    else:
        valor_interes = (dinero * porcentaje_interes * tiempo) / 12
        total_dinero = dinero+valor_interes
        return f"*El valor del Interés es de {valor_interes}\n*El total del dinero a retirar es {total_dinero}"