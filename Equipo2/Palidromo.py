#Programa que contenga una función que identifique si una palabra es un palíndromo o no.

def es_palindromo(frase):
    frase_limpia = frase.replace(" ", "").lower()
    
    if frase_limpia == frase_limpia[::-1]:
        print("Es un palindromo")
    else:
        print("NO es un palindromo")

frase_usuario = input("Introduce una palabra o frase: ")
es_palindromo(frase_usuario)
