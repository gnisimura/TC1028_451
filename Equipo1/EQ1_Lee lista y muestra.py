num = int(input("¿Cuántos items quieres que tenga tu lista?"))
while num<=0:
    num=int(input("¿Cuántos items quieres que tenga tu lista?"))
lista=list()
for x in range(num):
    n = input("Ingresa el elemento de tu lista")
    lista.append(n)

for i in range(len(lista)):
    print("lista[",i,"]=",lista[i])
