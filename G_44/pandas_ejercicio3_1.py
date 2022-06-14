""" Escribir una funcion que reciba un diccionario con las notas de los alumnos en curso en un examen
y devuelva una serie con la nota minima, la màxima, media y la desviación típica. """

import pandas as pd

notas={'Anderson': 3.3, 'Beatriz': 4.2, 'Camilo': 3.3, 'Dora': 4.5, 'Anthony': 2.3, 'Carlos': 2.2}

for keys in notas:
    notas[keys] = float(input(f'Digite la nota de {keys}: '))
    
print(notas)

def estadisticasNotas (notas):
    notas = pd.Series(notas)
    estadisticas = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index=['Nota Mínima','Nota Máxima','Nota Promedio','Desviación estandar'])
    return estadisticas

print(estadisticasNotas(notas))


