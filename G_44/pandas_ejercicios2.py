""" escribir un programa que pregunte al usuario por las ventas de un rango de años
y muestre por pantalla una serie con los datos de las ventas indexada por los años, 
antes y despues de aplicarles un descuento del 10% """

import pandas as pd

inicio = int(input('Digite el año de inicio de las ventas: '))
final = int(input('Digite el año de fin de las ventas: '))
ventas={} #diccionario donde guardamos las ventas {año: ventas}

for i in range(inicio, final+1):
   ventas[i] = float(input(f'Digite las ventas del año {i} $ :'))
print(ventas)

ventas = pd.Series(ventas) #diccionario a series
print('----serie de las ventas-----')
print(f'las ventas por años son: \n {ventas}')
print(f'las ventas por años con descuento: \n {ventas*0.9}')  # se aplica descuento



