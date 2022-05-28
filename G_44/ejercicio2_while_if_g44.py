def main():
    print ('Digite si, para continuar con el programa:  ')
    respuesta = (input('Desea continuar con el programa ? :'))
    
    while respuesta == "si":
        respuesta = (input('Desea continuar con el programa ? :'))
    
    print ('El programa ha terminado')
    
if __name__ == '__main__':
    main()
