test = input("Ingresa una frase: ")
li = list()
txt = test.replace(" ", "")

for i in range(len(txt)):
    li.append(txt[-i-1])

inv = ''.join(li)

if txt.lower() == inv.lower():
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
    
