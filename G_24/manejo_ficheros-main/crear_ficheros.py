import json

def guardar_info(info, nombre_fichero):
    with open(f'ficheros/{nombre_fichero}', 'w') as archivo:
        json.dump(info, archivo)

vehiculos = {
    'vehiculo_1': 'ART223',
    'vehiculo_2': 'RJQ554'
}

guardar_info(vehiculos, 'vehiculos.json')

persona = {
    'nombre': input('Nombre: '),
    'apellido': input('Apellido: '),
    'edad': int(input('Edad: '))
}
guardar_info(persona, 'persona.json')