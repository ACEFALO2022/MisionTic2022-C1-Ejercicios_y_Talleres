#1 Escribir un programa que almacene las asignatura de un curso(por ejemplo, matematica,fisica, quimica, historia y lengua en una lista y la muestre por pantalla)
#2 mostrar por pantalla el siguiente mensaje Yo estudio <asignatura>, donde asignatura es cada una de las asignaturas dela lista
#3 ahora que pregunta la nota de cada asignatura y despues las muestre por pantalla con el mensaje
# En <asignatura> has sacado <nota>
asignaturas=['matemáticas','fisica','quimica','historia','lengua']
notas=[]
print(asignaturas)
for i in asignaturas:
    n=(input(f'digite la nota para {i}: '))
    notas.append(n)
print('ha ingresado todas las notas')
print(asignaturas[1],notas[1])

# impresion de las listas
for i in range(len(asignaturas)):
    print('En',asignaturas[i], 'has sacado:',notas[i])
print('Hemos terminado')

    

    
