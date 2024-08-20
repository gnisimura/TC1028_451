def calcula_grado(x):
    if x<0 or x>1:
        print("score incorrecto")
    elif x>0.9 and x<=1:
        print("A")
    elif x>0.8 and x<=0.9:
        print("B")
    elif x>0.7 and x<=0.8:
        print("C")
    elif x>0.6 and x<=0.7:
        print("D")
    elif x<=0.6:
        print("F")
    
def main():
    x = float(input("Ingresa tu score: "))
    calcula_grado(x)

main()
    