distancia=0
dias=0
precio_ida=0
precio_regreso=0
billlete=0
descuento=30
precio_km=2.5
dias=int(input("ingrese la distancia que desea recorer  "))
distancia=int(input("ingrese los dias "))
regreso= distancia*2
if dias>7 and precio_ida>800:
    billlete=(precio_ida*2.5) * 0.7
    print ("el valor de billete es "+str(dias)+precio_ida+"regreso")
else:
     billlete=(precio_ida*2.5)
     print("el valor de billete es "+str(precio_regreso) +"es de")



""""descuento <- total*2.5
    total <- total - descuento
    precio_ida=(total)*2.5*0.7
    precio_regreso=total-descuento
print("presio-ida:", precio_ida)
print(" precio_regreso:", precio_regreso)
print("descuento :",descuento)"""""

##Determinar el precio de un billete de ida y vuelta en ferrocarril, conociendo la distancia a
##recorrer y sabiendo que si el número de dias de estancia es superior a siete y la distancia
#superior a 800 kilómetros el billete tiene una reducción del 30%. El precio por kilómetro es de
#2,5 dólares.
