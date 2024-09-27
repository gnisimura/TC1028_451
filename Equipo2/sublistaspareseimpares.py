
cantidad = int(input("Ingresa la cantidad de elementos que tendrá la lista: "))

lista_original = []

for _ in range(cantidad):
    valor = int(input())
    lista_original.append(valor)
    
pares = [x for x in lista_original if x % 2 == 0]
impares = [x for x in lista_original if x % 2 != 0]

# Muestra la lista original, los pares y los impares
print("LISTA ORIGINAL")
print(lista_original)

print("PARES")
print(pares)

print("IMPARES")
print(impares)
