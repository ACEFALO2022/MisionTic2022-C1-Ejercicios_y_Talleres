#escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:
import pandas as pd

mes=['Enero','Febrero','Marzo','Abril']
ventas=[]
gastos=[]

for i in mes:
    ventas.append(float(input(f'Ingrese el valor de las ventas en el mes {i}: ')))
    gastos.append(float(input(f'Ingrese el valor de los gastos en el mes {i}: ')))

#print(ventas)
#print(gastos)
datos={'Ventas':ventas,'Gastos':gastos}
contabilidad= pd.DataFrame(datos, columns=['Ventas','Gastos'], index=mes)
print (contabilidad)