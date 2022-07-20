c=0
n=int(input("Introduzca el extremos superior: "))  
n2=int(input("numero que desera saber los multiplos:"))
print("Múltiplos de :",n2)  
for i in range(1,n+n2):  
 if i%n2==0 :
  c+=1  
  print(i)  
print("Existen %i múltiplos de  ese rango, incluidos los extremos"%c,{n})  
