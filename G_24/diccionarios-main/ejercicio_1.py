'''
Calcule el promedio de notas del estudiante a partir 
del siguiente diccionario
'''

estudiante = {
    'nombre': 'Ana María',
    'apellido': 'López',
    'edad': 26,
    'notas': {
        'nota_1': 3.2,
        'nota_2': 3.0,
        'nota_3': 4.5,
        'nota_4': 4.2
    }
}

#Solución de Cristian
notas = estudiante['notas']
n1 = notas['nota_1']
n2 = notas['nota_2']
n3 = notas['nota_3']
n4 = notas['nota_4']

promedio = (n1+n2+n3+n4)/4

print(promedio)

#Solución de Sebastián
cantidadNotas = len(estudiante['notas'])

promedio = (estudiante['notas']['nota_1'] + estudiante['notas']['nota_2'] + estudiante['notas']['nota_3'] + estudiante['notas']['nota_4'] ) / cantidadNotas