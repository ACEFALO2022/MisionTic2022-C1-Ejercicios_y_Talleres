#crud para eliminar
estudiantesActivos={1512:['Angela Benavides'], 5478:['Anthony Racors'], 2530:['Camilo Jaramillo'], 5812:['Dora Saldaña']}

def numeroEstudiante(estudiantes,nombre):
    for identificacion,nombre in estudiantes.items():
        if nombre[0].lower()==nombreEstudiante.lower(): #lower convierte a minuscula si el usuario coloca en mayuscula
            return identificacion
    return 0
    

def imprimirEstudiantes(estudiantes):
    for identificacion, nombre in estudiantes.items() :  #.items() separa los items q estan en el diccionario key:valor
        print(f'El ID del estudiante es: {identificacion}')
        print(f'El Nombre del estudiante es: {nombre}')
        print('----------------')
        
print('Eliminar informacion')
eliminarEstudiante=int(input('Ingrese el Id del estudiante a eliminar: '))
if eliminarEstudiante in estudiantesActivos:
    nombreEstudiante = estudiantesActivos[eliminarEstudiante][0] 
    eliminarEstudiante = numeroEstudiante(estudiantesActivos, nombreEstudiante) #llama a la funcion de eliminar si existe el estudiante
    del estudiantesActivos[eliminarEstudiante]  
    imprimirEstudiantes(estudiantesActivos)
    print(f'El estudiante {nombreEstudiante} ha sido eliminado con exito')
else:
    print('El estudiante no encontrado')