#Triángulo
def dibuja_linea(x, typ="*"):
    print(x*typ)

def main(size):
    for i in range(size):
        dibuja_linea(i+1, car)

car = input("Ingresa un caracter con el que quieres hacer tu triángulo: ")
rep = int(input("Ingresa el tamaño del triángulo: "))

main(rep)
