def dibuja_linea(a,b):
    print(a*b)

Niveles = int(input("Ingrese la cantidad de niveles: "))
for i in range (1,Niveles+1,1):
    dibuja_linea("A",i)
