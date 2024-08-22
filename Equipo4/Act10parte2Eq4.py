def AreaRect(a,b):
    return a*b

def PerimetroRect(a,b):
    return (a*2)+(b*2)

def main():
    inp = input('Desea calcular el area (a) o perimetro (p) del rectangulo?\n')
    while inp.upper() !='A' and inp.upper() != 'P':
        inp = input('Error! Por favor ingrese a o p segun corresponda \n')
        print(inp.upper())
    
    try:
        ancho = float(input('Inserte el ancho del rectangulo \n'))
        largo = float(input('Inserte el largo del rectangulo \n'))
    except ValueError:
        ancho = float(input('Error, ingrese un numero, vuelva a insertar el ancho del rectangulo \n'))
        largo = float(input('Error, ingrese un numero, vuelva a insertar el largo del rectangulo \n'))


    if inp.upper() == 'A':
        print(f'El area del rectangulo es {AreaRect(ancho, largo)}')
    else:
        print(f'El perimetro del rectangulo es {PerimetroRect(ancho, largo)}')

if __name__ == "__main__":
  main()