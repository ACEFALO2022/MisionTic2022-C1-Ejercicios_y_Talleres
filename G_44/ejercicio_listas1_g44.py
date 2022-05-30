lista=['alex','andres','camilo','constanza','dora','fabian']
print(type(lista))
print(lista)

print('-------Longitud de la lista---len----')
print(len(lista)) 

print('-------Posicion de la lista-------')
print(lista[3]) 
print(lista[5])

print('-------Navegacion Inversa-------')
print(lista[-1]) 
print(lista[-3])

print('-------Imprimir un rango-------')
print(lista[2:5]) 
print(lista[1:4])

print('-------Cambiar elementos de una lista-------')
lista[2]='daniel'
print(lista)

print('-------Iterar una lista-----for x in lista--')
for n in lista:
    print(n)
    #print(n, end=' ')  #imprime horizontal la 
    
print('-------Revisar si un elemento de la lista existe-------')
if 'camilo' in lista:
    print('se encuentra en la lista')
else:
    print('No se encuentra en la lista')

print('-------Agregar elemento a una lista----append---')
lista.append('César')  #lo agrega al final de la lista
print(lista)

print('-------Agregar elemento en una posicion especifica a una lista----insert---')
lista.insert(3, 'Santiago')
print(lista)

print('-------Remover elemento por el nombre---remove---')
lista.remove('Santiago')
print(lista)

print('-------Remover ultimos elemento por el nombre----pop--')
lista.pop()
print(lista)

print('-------Remover elemento por la posicion------')
del lista[1]
print(lista)
del lista[1]
print(lista)

print('-------Eliminar por completo la lista    ---clear---')
lista.clear()
print(lista)
