
class Persona:
    
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
        
    def __str__(self) :
        
        #return '{} tiene, {} años' .format(self.nombre, self.edad)
        return f'{self.nombre} tiene, {self.edad} años'
    
personas=[
    Persona('Carlos',10),
    Persona('Andrea',25),
    Persona('Melisa',3),
    Persona('Mario',2)
]

menorEdad = filter(lambda Persona: Persona.edad<18,personas)
for menor in menorEdad:
    print(menor)