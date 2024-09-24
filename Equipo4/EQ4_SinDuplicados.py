lista = []
cont1=0
contrepetido = 0
num = int(input('Inserte el numero de elementos que tendra la lista: \n'))
for i in range(0,num):
    b = input('Escriba el elemento a agregar a la lista: \n')
    lista.append(b)
for i in lista:
    for j in range(lista.count(i)-1):
        lista.remove(i)
print(lista)