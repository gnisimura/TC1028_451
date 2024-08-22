largoRect=input()
anchoRect=input()
clave=input()
if clave=="a":
    arearect=(int(largoRect)*int(anchoRect))
    print("El area es", str(arearect))
elif clave=="p":
    perirect=(int(largoRect*2)+int(anchoRect*2))
    print ("El perimetro es", str(perirect))
else:
    print("no pues eso no existe")