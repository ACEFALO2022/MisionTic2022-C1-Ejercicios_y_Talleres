#4 Escribir un programa que almacene las asignaturas de un curso en una lista, pregunte al usuario la nota
# que ha sacado en casa asignatura y elimine de la lista las asignaturas aprobadas. Al final mostrar por pantalla
# las asignaturas que el usuario debe repetir.

asignaturas=['matemáticas','fisica','quimica','historia','lengua']
aprobado=[]
print(asignaturas)
for i in asignaturas:
    nota=float((input(f'digite la nota para {i}: ')))
    while nota > 5 or nota < 0:
        print('Ingrese una nota entre 0 y 5: ')
        nota=float((input(f'digite la nota para {i}: ')))
    else:
        if nota >=3:
            aprobado.append(i)
   # del asignaturas[i]

print('Ha terminado de ingresar las notas')

print('----lista de materias a repetir')     
for i in aprobado:    #recorre la lista aprobado
    asignaturas.remove(i)  #remueve lo que guarda en i temporalmente (lista aprobado) (elimina en lista asignatura lo coincide en las 2 listas)
print(f'tiene que repetir {asignaturas}') 
print('tiene que repetir', (asignaturas))   

    
