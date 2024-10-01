palabra = input('Inserte la palabra: ')
palabra2=palabra.replace(' ','')
palabra2=palabra2.lower()
if palabra2[::-1] == palabra2:
    print(f'{palabra} es un palindromo')
else:
    print(f'{palabra} no es un palindromo')