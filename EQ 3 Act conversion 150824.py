#Ingresar número
dist=float(input('Ingresa una número: '))
#Unidades
unit=input('¿Son km, m o cm?= ')
#Si no cumple con los requisitos
while not unit== 'km' and not unit== 'm' and not unit== 'cm':
    unid=input('Solo se aceptan respuestas como km, m o cm = ')
    if unid== 'km' or unid== 'm' or unid== 'cm':
        break

if unit== 'km':
    print('La equivalencia en metros es= ',dist*1000,'m')
    print('La equivalencia en centimetros es= ',dist*100000,'cm')
elif unit=='m':
    print('La equivalencia en kilómetros es= ',dist/1000,'km')
    print('La equivalencia en centímetros es= ',dist*100,'cm')
else:
    print('La equivalencia en kilómetros es= ',f'{dist/100000: .5f}','km')
    print('La equivalencia en metros es= ',dist/100,'m')
           