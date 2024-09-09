def dibuja_linea(char, cantidad):
    print(char * cantidad)

def main():
    n = int(input("Pon el valor de n: "))
    for i in range(1, n + 1):
        dibuja_linea('A', i)

main()
