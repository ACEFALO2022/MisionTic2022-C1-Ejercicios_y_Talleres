
supermercado = {
    'belen': {
        'aseo': 18000000,
        'frutas': 35000000
    },
    'poblado':{
        'aseo': 15000000,
        'frutas': 38000000
    }
}

sede_belen = supermercado['belen']
print(sede_belen)
aseo = sede_belen['aseo']
print(aseo)

print("------------------SOLUCIÓN DE MINIRETO---------------")

'''
1) Calcular el promedio de ventas por cada sede del supermercado
2) Obtener el TOTAl de VENTAS del supermercado
'''
#Solución de Camilo Andrés
superBelen = len(supermercado['belen'])
product1 = supermercado['belen']['aseo']
product2 = supermercado['belen']['frutas']
sub_total1 = product1 + product2
total1 = sub_total1 / superBelen

superPoblado = len(supermercado['poblado'])
product3 = supermercado['poblado']['aseo']
product4 = supermercado['poblado']['frutas']
sub_total2 = product3 + product4
total2 = sub_total1 / superPoblado

