def master():
    print ('confirmacion de contraseña ')
    password1= input('digite su contraseña: ')
    password2= input ('confirme su contraseña: ')
    
    while password1 != password2 :
        print('Las contraseñas son diferentes: ')
        password1= input('digite su contraseña: ')
        password2= input ('confirme su contraseña: ')
    print('Contraseña confirmada, su informacion ha sido registrada')

if __name__ == '__main__' :
    master()