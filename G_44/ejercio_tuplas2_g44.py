#almacenar en una lista de 5 elementos tuplas que guarden el nombre de un pais y la cantidad de habitantes
#Definir tres funciones, en la primera cargar la lista, en la segunda imprimirla y en la tercera mostrar el 
#nombre del pais con mayor cantidad de  habitantes.

def cargar():
    pais=[]
    for i in range(5):
        p=input(f'Ingrese el nombre de pais No {i+1} :  ')
        h=int(input(f'Ingrese poblacion pais No {i+1} :  '))
        pais.append((p,h))  #se guarda la informacion en una tupla dentro de la lista
    return(pais)

def imprimir(pais:list):
    print('paises y su poblaccion')
    for i in range(0,len(pais)):  #len me da el tamaño de la lista 
        print(pais[i][0], pais[i][1])       

def mayor(pais:list):
    pos=0
    for x in range(1,len(pais)): 
        if pais[x][1] > pais[pos][1]:  # compara la posicion 1 de las tupla (0,1) donde se guardó la cant de habitantes
            pos= x
    print(f'El pais con mayor cantidad de habitantes es: {pais[pos][0]} con {pais[pos][1]} habitantes', )        
    
# prueba del programa
pais=cargar() 
imprimir(pais) 
mayor(pais)  
