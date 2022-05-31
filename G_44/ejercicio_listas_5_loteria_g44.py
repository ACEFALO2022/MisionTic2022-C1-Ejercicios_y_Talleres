#4 Escribir un programa que pregunte al usuario los numeros ganadores de la loteria primitiva
# los almacene en una list y los muestre por pantalla ordenado de mayor a menor
 

loteria=[]
for i in range(6):
    loteria.append(int(input(f'digite el {i+1} numero ganador de la loteria : ')))
loteria.sort()

#print('los numeros ganadores son' + str(loteria))  
print(f'los numeros ganadores ordenado de  menor a mayor son {loteria}')
loteria.reverse()
print(f'los numeros ganadores ordenado de mayor a menor son {loteria}')