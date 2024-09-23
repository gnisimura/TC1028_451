num = int(input("¿Cuántos items quieres que tenga tu lista?"))
while num<=0:
    num=int(input("¿Cuántos items quieres que tenga tu lista?"))
lis1 = list()
lis2 = list()
lisres = list()


for x in range(num):
    n1 = input("Ingresa el elemento de tu lista")
    lis1.append(n1)
for x in range(num):
    n2 = input("Ingresa el elemento de tu lista")
    lis2.append(n2)
for i in range(len(lis1)):
    lisres.append(int(lis1[i])+int(lis2[i]))

print(lisres)