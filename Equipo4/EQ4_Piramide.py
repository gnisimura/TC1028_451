Niveles = int(input("Ingrese la cantidad de niveles: "))

for i in range (1,Niveles+1,1):
    print(" "*(Niveles-i), end="")
    print("* "*i) 
