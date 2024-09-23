a = True
lista, cont = [], 0
while a:
    b = int(input('Inserte un valor: \n'))
    if b >= 0:
        lista.append(b)
    else:
        a = False
for i in lista:
    if i % 2 == 0:
        cont +=1

print(f'El numero de pares es {cont} y de impares es {len(lista)-cont}')
        

