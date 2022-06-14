#Escribir una funcion que reciba un diccionario con las notas de los alumnos en curso en un examen y devuelva una serie con las notas de los alumnos aprobados ordenadas de mayor a menor.

import pandas as pd

notas={}

while True:
    nombre=str(input('Digite el nombre del alumno: '))
    nota= float(input(f'digite la nota para {nombre}: '))
    notas[nombre]=nota
    opcion=input('Desea continuar ingresando notas S/N: ' )
    if opcion.upper()=='N':  #toma no o No
        break

def aprobados(notas):
    notas=pd.Series(notas)
    return notas[notas>=3].sort_values(ascending= False) #ascendig false para ordenar ascendente

print('Los estudiantes aprobados son: ')
print(aprobados(notas))