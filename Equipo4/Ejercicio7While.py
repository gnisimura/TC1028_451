a=0
lista = []
while a >= 0:
    a = float(input('Inserte un numero de tipo flotante: \n'))
    lista.append(a)
x=0
for i in lista[:-1]:
    x+= i
if len(lista) > 1:
    promedio = x/(len(lista)-1)
    print(f'El promedio es {promedio}')
else:
    print('Solo pusiste un elemento negativo, no hay promedio')
    
