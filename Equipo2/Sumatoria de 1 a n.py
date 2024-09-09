def main():
    n = int(input("Pon un número entero positivo: "))
    suma_total = 0

    for i in range(1, n + 1):
        secuencia = "+".join(str(j) for j in range(1, i + 1))
        suma_parcial = sum(range(1, i + 1))  
        print(f"{secuencia} = {suma_parcial}")
        suma_total += suma_parcial 

    print(f"\nLa suma de la serie hasta el número {n} es: {suma_total}")

main()
