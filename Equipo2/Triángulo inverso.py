def dibuja_linea(char, cantidad):
    print(char * cantidad)

def main():
    n = int(input("Pon el valor de n: "))
    for i in range(n, 0, -1):
        dibuja_linea('0', i)

main()
