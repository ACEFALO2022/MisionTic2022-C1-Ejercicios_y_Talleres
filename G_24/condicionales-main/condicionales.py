#Booleanos
p = True
q = False
#Indicando el tipo de dato
r: bool = False

if q and p:
    print("And -> Es verdad")
else:
    print('And -> Es Falso')

if q or p:
    print('Or -> Verdad')
else:
    print('Or -> Falso')

if not p:
    print('Cumple')
else:
    print('No cumple')


if not (p and q or r and p):
    print("p and q or r and p -> Es verdad")
else:
    print("p and q or r and p -> Es Falso")


num_1 = 100
num_2 = 200
num_3 = 150

if num_1 >= num_2:
    print("Es mayor o igual")
elif num_1 < num_3:
        print("num_1 es menor a num_3")
else:
    print("No cumple ninguna condición")

opcion = "s"

if opcion == "s":
    print("Opción es 's'")
else:
    print("Opción es diferente de 's'")

if opcion != "s":
    print("Opción es diferente a 's'")