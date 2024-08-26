print("Escribe dos numeros donde a tiene que ser menor que b")
a= int(input("a:"))
b = int(input("b:"))
print("Los números pares en este rango son:")
while a<=b:
    if a%2!=0:
        a=a+1
    print(a)
    a=a+2