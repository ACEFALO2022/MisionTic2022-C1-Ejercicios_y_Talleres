#Convertir un objeto series con multiples listas en un unico objeto series
import pandas as pd

print('------Multiples listas en 1 objeto series--------')

datos = ['Colombia', 'Peru', 'Argentina'],['Bolivia','Uruguay'], ['Chile']
serie=pd.Series(datos)
print(serie)
serie=serie.apply(pd.Series) .stack().reset_index(drop=True) # a la serie inicial se vuelve a aplicar pd.series y se resetea el index
print(serie)

#Ordenar los valores de un objeto series con el metodo sort_values
print('------Odernar sort_values--------')
serieOrdenar= pd.Series(['1.1','Python','0.5','Pandas','200'])
print(serieOrdenar)
serieOrdenar = pd.Series(serieOrdenar).sort_values()
print(serieOrdenar) 

#Agregar datos a un objeto series existente
print('------OAgregar datos a serie existente--------')
serieOrdenar1= pd.Series(['1.1','Python','0.5','Pandas','200'])
serieOrdenar1= serieOrdenar1.append(pd.Series(['Java','HTML'])).reset_index(drop=True)
print(serieOrdenar1)

