#Al codigo ya existente que realizamos, vamos a actualizar uno de los datos de los estudiante y imprimiremos la lista de la totalidad de estudiantes activos
estudiantesActivos={1512:['Angela Benavides'], 5478:['Anthony Racors'], 2530:['Camilo Jaramillo'], 5812:['Dora Saldaña']}

print('Modificar Informacion')
idEstudiante =int(input('Digite el Id del estudiante: '))
estudiantesActivos[idEstudiante][0]=str(input('Digite el nuevo nombre: '))
print(f'El estudiante {estudiantesActivos[idEstudiante][0]}, ha sido modificado con exito')
print('----------------')

def imprimirEstudiante(estudiantes):
    for identificacion, nombre in estudiantes.items() :  #.items() separa los items q estan en el diccionario key:valor
        print(f'El ID del estudiante es: {identificacion}')
        print(f'El Nombre del estudiante es: {nombre}')
        print('----------------')
        

imprimirEstudiante(estudiantesActivos)