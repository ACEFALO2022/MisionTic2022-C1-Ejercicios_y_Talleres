# Un colegio quiere un programa que le permita ingresar un estudiante, y luego imprimir todos los estudiantes que esten activos, teniendo en cuenta
#que  el colegio tiene a los siguientes estudiantes ya cargados
 
estudiantesActivos={1512:['Angela Benavides'], 5478:['Anthony Racors'], 2530:['Camilo Jaramillo'], 5812:['Dora Saldaña']}

print('Carga estudiantes')
idEstudiante = int(input('Digite el ID del estudiante: '))  #variables globales
nombreEstudiante=str(input('Digite el Nombre del estudiante: ') ) #variables globales

def cargarEstudiante(identificacion:int, nombre:str):    #variables locales (identificacion=idEstudiante) (nombre=nombreEstudiante)
    estudiantesActivos[identificacion]=[nombre]
    print('Informacion cargada con exito')
    return estudiantesActivos

def imprimirEstudiante(estudiantes):
    for identificacion, nombre in estudiantes.items() :  #.items() separa los items q estan en el diccionario key:valor
        print(f'El ID del estudiante es: {identificacion}')
        print(f'El Nombre del estudiante es: {nombre}')
        print('----------------')
        
estudiantesActivos = cargarEstudiante(idEstudiante, nombreEstudiante)  #cargar la funcion con las variables globales
imprimirEstudiante(estudiantesActivos)
        
        
    