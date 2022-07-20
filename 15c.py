bisiesto=0
fin_de_mes = [31,28,31,30,31,30,31,31,30,31,30,31]
dia=int(input("por favor ingresar un dia "))
mes=int(input("por favor ingresar un mes "))
epoca=int(input("por favor ingresar un epoca "))

if epoca%4==0:
   if epoca%100==0:
      if epoca%400==0:
            fin_de_mes[1]=29
            bisiesto=True
      else:
            fin_de_mes=False
   else:
           fin_de_mes[1]=29
           bisiesto=True               
if bisiesto == True and mes == 2 :
    dia > 28 and dia == 1 
    print("el año no es bisiesto y el dia no es valido para el mes")
elif bisiesto and mes == 2 and dia < 28:
    print("el año es bisiesto")
else:
    print("el año no es bisiesto")

for i in range(len(fin_de_mes)):
    if mes- 1 == i:
        if dia >= 1 and dia < fin_de_mes[i]:
            dia += 1
            break
        else:
            day = 1
            mes += 1
            if mes > 12:
                mes = 1
                epoca += 1
            break


print("la fecha del dia siguiente es : ", dia, "._.", mes, "._.", epoca)     
    

