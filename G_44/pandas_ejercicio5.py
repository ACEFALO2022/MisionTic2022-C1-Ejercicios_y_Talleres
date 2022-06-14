#escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:
import pandas as pd

mes=['Enero','Febrero','Marzo','Abril']
datos=[[30500,22000],[35600, 23400],[28300, 18100],[33900, 20700]]

contabilidad= pd.DataFrame(datos, columns=['Ventas','Gastos'], index=mes)
print (contabilidad)