def fibonnaci_index(x):
    fib = list()
    first = 0
    second = 1
    fib.append(first)
    fib.append(second)
    pos=0
    while len(fib)<x+1:
        sec = fib[pos] + fib[pos+1]
        pos = pos+1
        fib.append(sec)
    print(fib[x-1])
            
place = int(input("Ingresa la posición de la secuencia de Fibonacci que deseas saber: "))           
            
fibonnaci_index(place)
            