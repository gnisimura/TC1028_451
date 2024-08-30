#pago de clientes
#Datos
precio=int(input('¿Cuál es el precio del artículo?: '))
articulos=int(input('¿Cuántos articulos va a comprar?: '))
otro=input('¿Desea comprar otro artículo? Coloca una S para sí y una N para no: ')
preciosum=precio*articulos

while otro=='S':
    precio2=int(input('¿Cuál es el precio del artículo?: '))
    articulos2=int(input('¿Cuántos articulos va a comprar?: '))
    
    articulos+=articulos2
    #suma de precios
    preciosum2=precio2*articulos2
    preciosum+=preciosum2
    
    otro=input('¿Desea comprar otro artículo? Coloca una S para sí y una N para no: ')

if otro != 'S':
    print('Numero de artículos comprados=', articulos)
    print('Total a pagar=',preciosum)
    