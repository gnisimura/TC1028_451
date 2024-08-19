a=int(input("a?"))
b=int(input("b?"))
c=int(input("c?"))

if a==b and b==c:
    print("Equilatero")
elif a==b or b==c or c==a:
    print("Isoscéles")
else:
    print("Escaleno")
    
if a+b<c or b+c<a or c+a<b:
    print ("No es un triángulo")
    
