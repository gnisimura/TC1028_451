#Dibuja linea
def dibuja_linea(x, typ="*"):
    print(x*typ)


car = input("Ingresa un caracter con el que quieres hacer tu linea: ")
rep = int(input("Ingresa el número de veces que quieres que se repita: "))

dibuja_linea(rep, car)