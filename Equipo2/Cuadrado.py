def dibuja_linea(char, cantidad):
    print(char * cantidad)

def main():
    n = int(input("Pon el valor de n: "))
    for _ in range(n):
        dibuja_linea('*', n)

main()
