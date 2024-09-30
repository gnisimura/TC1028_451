import math 

str1=str(input("Ingresa el string 1:"))
str2=str(input("Ingresa el string 2:"))

str11=str1[0:math.ceil(len(str1)/2)]
str12=str1[math.ceil(len(str1)/2):]

str21=str2[0:math.ceil(len(str2)/2)]
str22=str2[math.ceil(len(str2)/2):]


print(str(str11)+str(str22))
print(str(str12)+str(str21))


