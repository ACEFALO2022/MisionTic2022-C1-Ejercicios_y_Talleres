#tablas de multiplicar

numero=int(input('Digite el numero para la tabla de multiplicar: '))

for i in range (1,11):             # i toma los valores entre 1 y 10
    resultado= numero*i     
    print (f'{numero} x {i} = {resultado}')