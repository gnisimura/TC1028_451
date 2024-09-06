def dibuja_linea(caracter,cantidad):
    if cantidad>0:
        print(caracter*cantidad)
    elif cantidad<0:
        print('El valor no puedes ser negativo')

n=int(input('Ingresa la cantidad de lineas que desees: '))
caracter=input('Ingresa un caracter: ')

def main():
    
    for cantidad in range(n,0,-1):
        dibuja_linea(caracter,cantidad)

print('')
main()