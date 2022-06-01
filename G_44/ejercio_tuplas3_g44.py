#crea una tupla con los meses del año, pide numeros al usuario, si el numero
#esta entre 1 y la longitud maxima de la tupla, muestra el contenido de esa
#posicion sino muestra un mensaje de error
#el programa termina cuando el usuario introduceun cero

meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')

salir=False
while (not salir):
    
    numero=int(input('Digite un numero: '))
        
    if numero==0 :
        salir= True
    else:
        if (numero>=1 and numero<= len(meses)):
            print(meses[numero-1])
        else:
            print('Ingrese un numero entre 1 y ', len(meses))