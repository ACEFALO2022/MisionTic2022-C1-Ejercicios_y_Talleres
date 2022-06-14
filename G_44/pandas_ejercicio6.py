#Escribir una funcion que reciba un DataFrame con el formato del ejercicio anterior, una lista de meses, y devuelva el balance (ventas-gastos) total en los meses indicados
import pandas as pd
datos={'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'], 'Ventas':[30500,35600,28300,33900], 'Gastos':[2200,23400,18100,33900]}

contabilidad=pd.DataFrame(datos)

def balance(contabilidad,meses):
    contabilidad['Balance']=contabilidad.Ventas - contabilidad.Gastos
    return contabilidad[contabilidad.Mes.isin(meses)].Balance.sum()

    