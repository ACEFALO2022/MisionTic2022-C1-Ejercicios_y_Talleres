#Aplicr las operaciones aritmetica sobre objetos series

import pandas as pd

serie2=pd.Series([1,2,3,4,5])
serie3=pd.Series([7,2,8,4,9])
print(serie2)
print(serie3)
print('------Operaciones aritmeticas con series--------')
print(serie2 + serie3)
print(serie2 - serie3)
print(serie2 / serie3)
print(serie2 * serie3)

#convertir un diccionario python en objeto Series
print('------diccionario a serie--------')
datos = {'A':10,'B':20,'C':30}
print(type(datos))
print(datos)
series=pd.Series(datos)
print(type(series))
print(series)

#convertir un arreglo Numpy en un objeto series
print('------Array Numpy a serie--------')
import numpy as np
arreglo = np.array([1,2,3,4,5])
print(arreglo)
seriea=pd.Series(arreglo)
print(seriea)

#Cambiar el tipo de datos de un objeto serie
print('-----Cambiar el tipo de datos de un objeto serie--------')
tdatos = pd.Series(['100','200','300','400','Minios','500.2'])
print(tdatos)
tdatos=pd.to_numeric(tdatos, errors='coerce')  #forza a q muestre error si el dato no es numerico
print(tdatos)

#Obtener una columna de un objeto DataFrame como un objeto Series
print('-----columna DataFrame de un objeto serie--------')
dataF= {'A':[1,2,3,4], 'B':[5,6,7,8], 'C':[9,10,11,13]}
df=pd.DataFrame(data=dataF)
print(df)
print()
columna=df.iloc[:,2]
print(columna)

#Extraer una fila de un DataFrame como un ojeto Series
print('-----Fila----)')
fila=df.iloc[0,:]
print(fila)
print(df.iloc[2,1])
