#Triángulo inverso
def dibuja_linea(x, typ="*"):
    print(x*typ)

def main(size):
    for i in range(size, 0, -1):
        dibuja_linea(i, car)


car = input("Ingresa un caracter con el que quieres hacer tu linea: ")
rep = int(input("Ingresa el tamaño del triángulo: "))

main(rep)