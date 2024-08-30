
clave = ''
costo = 0
productos = ''

A = 120
B = 250
C = 360

producto_a = 'A - '
producto_b = 'B - '
producto_c = 'C - '


while not clave == 'X':
    clave = input('Escriba la clave del producto: ')
    
    if clave == 'A':
        costo = costo + A
        print(producto_a + str(A))
    elif clave == 'B':
        costo = costo + B
        print(producto_b + str(B))
    elif clave == 'C':
        costo = costo + C
        print(producto_c + str(C))

print('Costo: ' + str(costo))
