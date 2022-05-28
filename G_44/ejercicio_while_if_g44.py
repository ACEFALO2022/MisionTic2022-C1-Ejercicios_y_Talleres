
def main():
    print ('Alcancia Digital')
    objetivo=float(input('Cuanto desea ahorrar:  '))
    ahorrado=0
    
    while objetivo>ahorrado:
        ahorrado+=float(input('Cuanto va a abonar: '))
    
    print (f'Ha cumplido con la meta, su ahorro es {ahorrado} le sobra {ahorrado-objetivo}')
    
if __name__ == '__main__':
    main()
    
    
