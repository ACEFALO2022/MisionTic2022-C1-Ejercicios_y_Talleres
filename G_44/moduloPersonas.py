#creacion de una clase llamada Persona

class Persona:
    
    def __init__(self,nombre,edad, genero):  #__init__ siempre se usa para iniciar una clase
        self.__nombre = nombre
        self.__edad = edad
        self.__genero = genero
        
    def __str__(self) :
        
        return 'El nombre es : ' + self.__nombre + ' y su edad es: ' + str(self.__edad) + ' su genero es: ' + self.__genero