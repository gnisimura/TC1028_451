#tipos de envio
pt = input("¿Tú producto es un descargable o un envio? ")
ptt = pt.lower()
if ptt=="envio" or ptt=="envío":
    tipo = "e"
elif ptt=="descargable" or ptt=="descarga":
    tipo = "d"

#Monto de compra
mc = float(input("¿De cuánto es el monto de su compra?(en USD)"))
#datos de salida


#tarjeta VIP
pv = input("¿Cuenta con tarjeta VIP? ")
vip = pv.lower()

imp=0
gasEnv=0
#Lugar de destino
if tipo=="e":
    #impuestos por continente
    continent = input("¿A qué continente haremos el envío? ")
    cont = continent.lower()
    if cont == "america" or cont=="américa":
        imp = mc * 5/100
    elif cont=="europa":
        imp = mc*12/100
    elif cont=="asia":
        imp= mc*8/100
    #Gastos de envío
    peso = float(input("¿Cuál es el peso de su paquete?(en kg)"))
    if peso<5:
        gasEnv=35
    elif peso >= 5:
        dif= peso-5
        gasEnv= 35 + (dif*5)

#descuentos
if vip=="si" or vip=="sí":
    desc = mc * 20/100
elif vip=="no" and mc>5000:
    desc = mc*12/100
else:
    desc = 0

#datos de salida
print("El monto de tu compra es:", mc, "USD")
print("Tus descuentos son:", desc)
print("Tus impuestos son:", imp, "USD")
print("Los gastos de tu envío son", gasEnv, "USD")
total= mc + imp - desc + gasEnv
print("El total de tu compra es de:", total, "USD")
