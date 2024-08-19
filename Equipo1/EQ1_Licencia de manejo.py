age=float(input("¿Cuántos años tienes? "))
print("¿Tienes identificación oficial?")
ide=input("s para si, n para no")
while not ide=="s" and not ide=="n":
    ide=input("Favor de utilizar solo 's' para si y 'n' para no")
    if ide=="s" or ide=="n":
        break
    
if age>=18 and ide=="s":
    print("Si puedes tener tu licencia de manejo")
else:
    print("No puedes tener tu licencia de manejo")
