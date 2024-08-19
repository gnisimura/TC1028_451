#Ingresar números
x=int(input('Valor de x: '))
y=int(input('Valor de y: '))
z=int(input('Valor de z: '))
if x>y and x>z:
    print('El número mayor es',x)
elif y>x and y>z:
    print('El número mayor es', y)
else:
    print('El número mayor es', z)
