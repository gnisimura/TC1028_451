texto = str(input("Ingrese texto: "))

#longitud del string
print(len(texto))

#primer caracter
print(texto[0])

#ultimo caracter
print(texto[-1])

#caracteres con indice impar
for x in range(0, len(texto)):
    if x % 2 != 0:
        print(texto[x], end="")
