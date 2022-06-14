#Escribir una funcion que reciba un diccionario con las notas de los alumnos en curso en un examen y devuelva una serie con las notas de los alumnos aprobados ordenadas de mayor a menor.

import pandas as pd

notas={'Anderson': 3.3, 'Beatriz': 3.5, 'Camilo': 3.6, 'Dora': 4.0, 'Anthony': 4.1, 'Carlos': 5.0}

def aprobados(notas):
    notas=pd.Series(notas)
    return notas[notas>=3].sort_values(ascending= False)  #ascendig false para ordenar ascendente

print(aprobados(notas))