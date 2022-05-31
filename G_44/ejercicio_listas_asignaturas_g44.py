#1 Escribir un programa que almacene las asignatura de un curso(por ejemplo, matematica
# fisica, quimica, historia y lengua en una lista y la muestre por pantalla)
print('-------con while--------')
asignaturas=[]
contador=1
total=int(input(f'cuantas asignaturas desea guardar: '))

while contador <= total:
    n=input(f'Digite asignatura a guardar:  ')
    asignaturas.append(n)
    contador+=1

print('Asignaturas Guardadas')
print(asignaturas)

print('------con for--------')
materias=[]
total2=int(input(f'cuantas asignaturas desea guardar: '))

for n in range(1,total2 + 1):
    a=input(f'Digite asignatura a guardar:  ')
    materias.append(a)


print('Asignaturas Guardadas')
print(materias)

