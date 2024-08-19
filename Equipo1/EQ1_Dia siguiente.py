year = int(input("Introduzca el año: "))
month = int(input("Introduzca el mes(número): "))
day = int(input("Introduzca el día: "))
if year%4==0:
    if month==2:
        if day==29:
            print("El día siguiente es: ", year, "/", month+1,"/", "1" )
            exit()
        else:
            print("El día siguiente es: ",year,"/", month,"/", day+1)    

if month==12 and day==31:
    print("El día siguiente es: ", year+1, "/", "1","/", "1" )
    exit()
    
if month==2:
    if day==28:
        print("El día siguiente es: ", year, "/", month+1,"/", "1" )
        exit()
    else:
        print("El día siguiente es: ",year,"/", month,"/", day+1)

if month%2==1 or month==8:
    if day==31:
        print("El día siguiente es: ", year, "/", month+1,"/", "1" )
        exit()
    else:
        print("El día siguiente es: ",year,"/", month,"/", day+1)
if month%2==0:
    if day==30:
        print("El día siguiente es: ", year, "/", month+1,"/", "1" )
        exit()
    else:
        print("El día siguiente es: ",year,"/", month,"/", day+1)

