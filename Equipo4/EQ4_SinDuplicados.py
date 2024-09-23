lista = []
cont1=0
contrepetido = 0
num = int(input('Inserte el numero de elementos que tendra la lista: \n'))
for i in range(0,num):
    b = input('Escriba el elemento a agregar a la lista: \n')
    lista.append(b)
print(lista)
for i in lista:
    if i == lista[cont1]:
        contrepetido +=1
    if contrepetido > 1:
        lista.remove(i)
    cont1 +=1
print(lista)