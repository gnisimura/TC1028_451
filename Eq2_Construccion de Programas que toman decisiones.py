
x = input("Escriba la longitud del lado 1: ")
y = input("Escriba la longitud del lado 2: ")
z = input("Escriba la longitud del lado 3: ")

if x + y > z and x + z > y and y + z > x:
    print("Es un triángulo rectangulo")
    if x == z or x == y or y == z:
        print("Es un triánugulo isosceles")
    elif x == y and y == z:
        print("Es un triangulo equilatero")
    else:
        print("Es un triangulo escaleno")
else:
    print("No es un triangulo")
