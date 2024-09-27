col=int(input("Columnas?"))
fil=int(input("Filas?"))
matriz=[]
for i in range (fil):
    fila=[]
    for j in range (col):
        dato=int(input("Dato en la fila "+ str(i+1) +" y columna "+str(j+1)))
        fila.append(dato)
    matriz.append(fila)
    
print(matriz) 
listapares=[]
for i in range(fil):
    pares=0
    for j in range(col):
        if int(matriz[i][j])%2==0:
            pares+=1
    listapares.append(pares)
    
print(listapares)
    
        