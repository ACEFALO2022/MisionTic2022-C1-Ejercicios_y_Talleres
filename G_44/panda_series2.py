#crear y visualizar un arreglo unidimensional como una estructura de series

import pandas as pd

datos= [2,3,5,7,11]
serie = pd.Series(datos)
print(serie)
print(serie.size)
print(serie.describe())  #describe la serie
print('')

#convertir un objeto series a una lista python

datos1= [2,3,5,7,11]
serie1 = pd.Series(datos)
print(type(datos1))
print(type(serie1))

lista= serie1.tolist()
print(type(lista))
print(lista)

#usar operadores relacionales para comparar objetos series
print('---comparar series--------')

serie4=pd.Series([1,2,3,4,5])
serie5=pd.Series([7,3,5,6,2])
print(serie4)
print(serie5)
print(serie4 < serie5)
print(serie4 > serie5)
print(serie4 == serie5)

