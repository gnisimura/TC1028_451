print("Ingresa las columnas y filas (>=2): ")
col = int(input("Columnas: "))
ren = int(input("Filas: "))
while col<2 or ren<2:
    print("Error")
    col = int(input("Columnas: "))
    ren = int(input("Filas: "))

mat = list()
rowsh = list()
n =1

for renglones in range(ren):
    rowsh = list()
    for colu in range(col):
        rowsh.append(n)
        n = n+1
    mat.append(rowsh)
print(mat)
    