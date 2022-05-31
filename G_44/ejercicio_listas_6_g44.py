#4 Escribir un programa que almacene en una lista los numeros de 1 al 10 y los muestre en pantalla
# en modo inverso separado por comas
'''
numeros=[]
for i in range(10):
    numero=(int(input(f'digite el {i+1} numero : ')))
    
    while numero<0 or numero > 10:
        numero=(int(input(f'digite el {i+1} numero : ')))
    else:
        numeros.append(numero)
        
numeros.sort()
numeros.reverse()

print(f'los numeros ordenados en reversa  {numeros}')
'''''
    
print('--------solucion 2------')

numbers=[1,2,3,4,5,6,7,8,9,10]
for i in range(1,11):
    #print(numbers[-i], end=', ''\n')
    print(numbers[-i], end=', ')
    

print('\n')
print('--------solucion 3------')

numbers=[1,2,3,4,5,6,7,8,9,10]
numbers.reverse()
for number in numbers:
    print(number, end=', ')