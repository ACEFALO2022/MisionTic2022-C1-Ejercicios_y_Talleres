#1 Escribir un programa que almacene las asignatura de un curso(por ejemplo, matematica,fisica, quimica, historia y lengua en una lista y la muestre por pantalla)
#2 mostrar por pantalla el siguiente mensaje Yo estudio <asignatura>, donde asignatura es cada una de las asignaturas dela lista


asignaturas=['matemáticas','fisica','quimica','historia','lengua']
print(asignaturas)
i=0
for i in asignaturas:
    print(f'yo estudio, {i}')
print('No hay mas materias')