
import json

persona = {}
def abrir_archivo(ruta: str):
    cadena: list = ruta.split('.')
    if cadena[1].lower() == 'json':
        try:
            #Referencias el fichero
            with open(ruta) as archivo:
                #Cargar los datos del archivo json
                persona = json.load(archivo)
                print(persona)
        except:
            print('Error al cargar los datos')
    else:
        print('Extensión inválida')

abrir_archivo('persona.json')

#Referenciar el fichero
""" with open('personas.json','w') as archivo:
    #Escribir/crear el fichero
    json.dump(persona, archivo) """
