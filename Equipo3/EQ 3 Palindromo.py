frase = input('Escribe una frase: ')

palabra = frase.replace(" ","").lower()

if palabra == palabra[::-1]:
    print('Es un palíndromo')
else:
    print('No es un palíndromo')