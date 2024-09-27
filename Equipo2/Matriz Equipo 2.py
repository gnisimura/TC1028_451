

num = int(input("Escriba la cantidad de columnas y renglones que desea tener en la matriz: "))

matriz = list()

for x in range(num):
    lista = []
    for i in range(num):
        lista.append(x)
    matriz.append(lista)

        


print(matriz)
