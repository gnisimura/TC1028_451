val1 = float(input("Escribe un numero: "))
val2 = float(input("Escribe un segundo numero: "))

res = float()

print(
"""Escriba la letra para la operacion que quieres realizar: 

s = suma
r = resta
m = multiplicacion
d = division

""")

operacion  = str(input())



def Operacion(x, y):
    if operacion == "s":
        res = x + y
        return res
    elif operacion == "r":
        res = x - y
        return res
    elif operacion == "m":
        res = x * y
        return res
    elif operacion == "d":
        if y == 0:
            print("Da error al dividir entre cero")
        else:
            res = x / y 
            return res
    else:
        print("No es una de las opciones de operacion")

print("El resultado es " + str(Operacion(val1, val2)))