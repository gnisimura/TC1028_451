col = int(input('Inserte el numero de columnas'))
fil = int(input('Inserte el numero de filas'))
matriz=[]
for i in range(fil):
    matriz.append([])

for j in range(fil):
    for k in range(col):
        print(f'Inserte el valor en la fila {j+1} y columna {k+1}')
        a = int(input())
        matriz[j].append(a)
cont2 = 0 
for h in matriz:
    cont = 0
    cont2 +=1
    for n in range(col):
        if h[n]%2 == 0:
            cont +=1
    print(f'El numero de pares en el renglon {cont2} es {cont}')
    