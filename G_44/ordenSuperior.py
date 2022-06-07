def convertir (sis) :
    
    def sis_bin(numero):
        print(f'El numero decimal:  {numero}, en binario es {bin(numero)}')
    
    def sis_oct(numero):
        print(f'El numero decimal:  {numero}, en octal es {oct(numero)}')
        
    def sis_hex(numero):
        print(f'El numero decimal:  {numero}, en hexadecimal es {hex(numero)}')
    
    sis_fun = {'bin': sis_bin, 'oct': sis_oct, 'hex': sis_hex} #en un diccionario si se llama 'bin' se ejecuta sis_bin etc etc
    return sis_fun[sis]    # se ejecuta sis_fun cuando se le da el parametro [sis]
        
numeroC=int(input('Digite el numero a convertir: '))
convertir ('bin')(numeroC)
convertir ('oct')(numeroC)
convertir ('hex')(numeroC)