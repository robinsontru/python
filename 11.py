menor=0
centarl=0
mayor=0
mayor = int(input("Introduce el número :"))
centarl = int(input("Introduce el número :"))
menor= int(input("Introduce el número :"))
lista=[mayor,centarl,menor]
for numero in lista:
  if menor ==0 and centarl ==0 and  mayor==0 :
     menor==numero
     ##centarl=numero
     mayor==numero
    
  else:
      if numero<menor:
        menor=numero
        ##centarl=numero
        if numero>mayor:
           mayor=numero
           centarl=numero
           
print("el numero central es",{centarl},{mayor}, {menor})
