palabra = input('Inserte la palabra: ')
palabra.replace(' ','')
if palabra[::-1] == palabra:
    print(f'La palabra {palabra} es un palindromo')
else:
    print(f'La palabra {palabra} no es un palindromo') 