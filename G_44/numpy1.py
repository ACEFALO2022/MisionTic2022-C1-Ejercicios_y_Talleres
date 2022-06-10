import numpy as np

#Crear un vector con valor dentro del rango 10 a 49 (arreglo es como se llaman a las listas en numpy)
print ('------Crear un vector---')
a= np.arange(10,50)
print(a)

print ('------invertir un vector---')
print(a[::-1])

print ('------crear un vector 3x3--con valores de 0 al 8----')
print(np.arange(0,9) .reshape(3,3))

print ('--- vector 4x3------')
print(np.arange(0,12) .reshape(4,3))
print ('------3x4----')
print(np.arange(0,12) .reshape(3,4))

#Encontrar los indices que no son ceros del arreglo [1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0]

print ('--- Encontrar indices con argwhere------')
a=np.array([1,2,4,2,4,0,1,0,0,0,12,4,5,6,7,0])
print(np.argwhere(a!=0))
print('--------------')
print(np.argwhere(a==0))

#crear una matriz identidad de 6x6
print ('--- matriz identidad de 6x6---identity---')
print(np.identity(6))

#crear una matriz con valores al azar con forma 3x3x3
print ('--- matriz tres dimensiones 3x3x3---.random.random------')
r=np.random.random((3,3,3))
print(r)

#Encontrar los indices de los valores minimos y maximos de la anterior matriz
print ('--- indice valor minimo------')
print(r.argmin())
print(r.ravel() [r.argmin()])

print ('--- indice valor maximo------')
print(r.argmax())
print(r.ravel() [r.argmax()])

#crear una matriz de 10x10 con 1's en los bordes y 0 en el interior ( con rangos de indices)
print ('--- matriz 10x10 bordes (1), interior (0)------')
z=np.ones((10,10))  #.ones se llena con (1) una matriz
z[1:-1,1:-1]=0
print(z)

#crear una matriz de 5x5 con valores en los renglones que vayan de 0 a 4
print ('--- matriz 5x5 con tile------')
print(np.tile(np.arange(0,5),5).reshape(5,5))  #.tile repite el arreglo n veces para completar la matriz

#crear dos arreglos al azar A y B, verificar si son iguales
print ('--- Verificar si son iguales 2 matrices al azar------')
a=np.random.random((4,2))
c=np.random.random((4,2))
print(a==c)
