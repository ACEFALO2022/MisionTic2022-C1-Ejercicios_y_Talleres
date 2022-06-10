import numpy as np

#Array de una dimension
a1=np.array([1,2,3])
print(a1)
print()

#Array de dos dimensiones
a2=np.array([[1,2,3],[4,5,6]])
print(a2)
print(a2[1][0])
print(a2[0][1])
print()

#Array de tres dimensiones
a3=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(a3)

#operaciones matematicas
print('----operaciones entre matrices ------')
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,1,8],[10,7,11]])
print(a+b)
print()
print(b**2)

