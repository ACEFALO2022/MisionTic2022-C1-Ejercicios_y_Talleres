#Obtener las primeras n filas de un objeto DataFrame
print('Actividad 1 Data Frame')
import pandas as pd
import numpy as np

nombre=['anderson', 'angela','anthony','beatriz','clara', 'dora', 'daniel', 'elena', 'fabian']
puntaje=[11.3, 5.8, 15.5, np.nan , 8, 9, 13.5, np.nan, 17]
intentos = [1,2,3,4,5,6,1,2,3]
califico=['si','no','no','no','si','si','si','si','no']
indices=['a','b','c','d','e','f','g','h','i']
jugadores={'nombre':nombre,'puntaje':puntaje,'intentos':intentos,'califico':califico}
df = pd.DataFrame(data=jugadores, index = indices)
print(df)
print('-------n-filas--------')
print(df.iloc[0:3])
print('------ultima-fila-------')
print(df.iloc[-1:])
#Obtener los ejes (atributos de filas y colu) de un DataFrame
print('------atributos--------')
print(df.axes)

#Obtener la representacion en Numpy de un objeto DataFrame
print('-------DataFrame-a--Numpy------')
datos={'x':[1,2,3,4,5], 'y':[5,4,3,2,1], 'z':[6,7,8,9,10]}
dfram=pd.DataFrame(data= datos)
print(dfram)
anumpy=(dfram.to_numpy())
print(anumpy)



