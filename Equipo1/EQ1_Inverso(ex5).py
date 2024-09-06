#Equipo 1: Inverso
n=int(input("Ingresa un número de hasta 6 dígitos para dartelo invertido: "))

conv = str(n)
lett = list(conv)
rev = list()
n=len(lett)-1

if len(conv)>7 and conv.startswith("-")==True:
    print("numero demasiado largo")

elif len(conv)>6 and conv.startswith("-")==False:
    print("numero demasiado largo")
    
else:
    if conv.startswith("-")==True:
        rev.append(lett[0])
        while n>1:
            for i in range(n):
                rev.append(lett[n])
                n = n-1
            
    elif conv.startswith("-")==False:
        for i in range(len(lett)):
            rev.append(lett[n])
            n = n-1
            
    inum = ''.join(rev)
    print("El inverso de tu número es", inum)

