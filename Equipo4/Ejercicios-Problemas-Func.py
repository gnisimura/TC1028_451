def Area_cilindro(r,a):
    return 2*3.1416*r**2+2*3.1416*r*a

def Volumen_cilindro(r,a):
    return 3.1416*r**2*a

def main():
    try:
        radio = float(input('Inserte el radio del cilindro \n'))
        altura = float(input('Inserte la altura del cilindro \n'))
    except ValueError:
        radio = float(input('Error, ingrese un numero, vuelva a insertar el radio del cilindro \n'))
        altura = float(input('Error, ingrese un numero, vuelva a insertar la altura del cilindro \n'))


    print(f'El area del cilindro es {round(Area_cilindro(radio,altura),2)}')
    print(f'El volumen del cilindro es {round(Volumen_cilindro(radio, altura),2)}')

if __name__ == "__main__":
  main()
