cantidad = int(input("¿Cuántos números deseas poner? "))


numeros = []

for i in range(cantidad):
    numero = int(input(f"Introduce el número {i+1}: "))
    numeros.append(numero)



numeros.reverse()


print("Lista al revés:", numeros)