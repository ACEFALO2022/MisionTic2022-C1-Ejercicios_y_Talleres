frutas=('naranja','pera','uva','banana')
print(frutas)

print('-----dimension de una tupla----')
print(len(frutas))

print('-----acceder a una tupla----')
print(frutas[2])

# print('-----La tupla es inmutable----')
# frutas[0]='papaya'
# print(frutas)

print('-----Convertir tupla en lista para modificarla----')
frutasLista = list(frutas)  #convertir tupla en lista
frutasLista[0]='papaya'
frutas=tuple(frutasLista)  #convertir la lista en tupla
print(frutas)

print('-----Iterar una tupla----')

for fruta in frutas :
    print(fruta,end='-') # end para mostrar en horizontal
    
#