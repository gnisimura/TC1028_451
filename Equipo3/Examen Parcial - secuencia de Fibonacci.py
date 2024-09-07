def fibonacci_index(index):

    if index == 0:
        return 0
    elif index == 1:
        return 1

    a, b = 0, 1

    for i in range(2, index + 1):
        
        a, b = b, a + b
    
    
    return a

index = int(input("Ingresa el índice de la secuencia de Fibonacci que quieres conocer: "))

print(fibonacci_index(index))
