def fibonacci_index(n):
    c=3
    fib_1=0
    fib_2=1
    fib_3=0
    while c<=n:
        fib_3=fib_1+fib_2
        fib_1=fib_2
        fib_2=fib_3
        c=c+1
        
    print(fib_3)
    
posicion=int(input("Que numero de fibbonacci quieres sacar?"))

if posicion==1:
    print(0)
elif posicion==2:
    print(1)
elif posicion==3:
    print(1)
else:
    fibonacci_index(posicion)
        
    